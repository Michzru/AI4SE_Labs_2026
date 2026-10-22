"""Offline tests of the deterministic nodes (run: python -m unittest test_step1 -v)."""
import unittest

from network import build_graph, squash, verify_evidence


class VerifyEvidenceTest(unittest.TestCase):
    def state(self, evidence, chunk_text="> Staff must be able to\n> log in with\n> their ID — fast!"):
        return {
            "chunks": [{"doc_id": "a.eml", "index": 0, "total": 1, "text": chunk_text}],
            "raw_candidates": [{"title": "t", "description": "d", "evidence": evidence,
                                "type": "functional", "date": None,
                                "doc_id": "a.eml", "chunk_index": 0}],
        }

    def test_quote_survives_wrapping_prefixes_and_dashes(self):
        c = verify_evidence(self.state("Staff must be able to log in with their ID - fast!"))["candidates"][0]
        self.assertTrue(c["evidence_ok"])
        self.assertEqual((c["id"], c["source_doc"]), ("C001", "a.eml"))

    def test_invented_quote_is_flagged_not_dropped(self):
        c = verify_evidence(self.state("Staff must log in with a fingerprint"))["candidates"]
        self.assertEqual(len(c), 1)
        self.assertFalse(c[0]["evidence_ok"])

    def test_empty_quote_is_flagged(self):
        self.assertFalse(verify_evidence(self.state(""))["candidates"][0]["evidence_ok"])

    def test_ids_are_stable_regardless_of_arrival_order(self):
        st = self.state("x")
        base = st["raw_candidates"][0]
        st["chunks"].append({"doc_id": "a.eml", "index": 1, "total": 2, "text": "x"})
        st["raw_candidates"] = [{**base, "chunk_index": 1, "title": "second"}, {**base, "title": "first"}]
        self.assertEqual([c["title"] for c in verify_evidence(st)["candidates"]], ["first", "second"])


class GraphTest(unittest.TestCase):
    def test_squash(self):
        self.assertEqual(squash("A’b - C\n d"), "abcd")

    def test_partial_graph_runs_without_api(self):
        graph = build_graph(stop_after="chunk_documents")
        self.assertIn("chunks", graph.invoke({"input_dir": "data/corpus"}))


if __name__ == "__main__":
    unittest.main()


class FeedbackLoopTest(unittest.TestCase):
    """The loop with fake LLM nodes: reviewer always finds something, the cap must stop it."""

    def test_loop_stops_at_cap_and_only_reextracts_flagged_docs(self):
        import network
        calls = {"extract": [], "review": 0}

        def fake_extract(task):
            calls["extract"].append((task["chunk"]["doc_id"], task.get("feedback")))
            return {"raw_candidates": [{"title": "t", "description": "d", "evidence": "x", "type": "functional",
                                        "date": None, "doc_id": task["chunk"]["doc_id"],
                                        "chunk_index": task["chunk"]["index"]}]}

        def fake_review(task):
            calls["review"] += 1
            missing = [{"description": "gap", "evidence": "x", "quote_ok": True}] if task["doc"]["id"] == "a" else []
            return {"reviews": [{"doc_id": task["doc"]["id"], "round": task["round"], "missing": missing}]}

        calls["merge"] = 0

        def fake_merge(state):
            calls["merge"] += 1
            return {"requirements": [], "blacklist": []}

        fakes = {**network.NODES, "extract": fake_extract, "review_completeness": fake_review,
                 "merge_and_resolve": fake_merge}
        state = {"documents": [{"id": "a", "text": "x"}, {"id": "b", "text": "x"}],
                 "chunks": [{"doc_id": d, "index": 0, "total": 1, "text": "x"} for d in "ab"]}
        old, network.NODES = network.NODES, fakes
        try:
            result = network.build_graph("extract", "merge_and_resolve").invoke(state)
        finally:
            network.NODES = old
        self.assertEqual(result["iteration"], 3)            # initial review + 2 re-extractions
        self.assertEqual([d for d, f in calls["extract"] if f], ["a", "a"])   # b never re-extracted
        self.assertEqual(calls["review"], 6)                # 2 docs x 3 rounds
        self.assertEqual(result["feedback"], {})
        self.assertEqual(calls["merge"], 1)                 # merge runs once, after the loop ended


class ReviewGateTest(unittest.TestCase):
    def test_ignores_items_with_unverified_quote(self):
        from network import review_gate
        state = {"iteration": 0, "reviews": [{"doc_id": "a", "round": 0, "missing": [
            {"description": "real", "evidence": "q", "quote_ok": True},
            {"description": "invented", "evidence": "z", "quote_ok": False}]}]}
        out = review_gate(state)
        self.assertEqual(out["feedback"], {"a": "- real"})
        self.assertEqual(out["iteration"], 1)


class ApplyMergeTest(unittest.TestCase):
    def items(self):
        from merge import to_item

        def c(i, doc, title, typ="functional", date=None, ok=True):
            return to_item({"id": i, "title": title, "description": "d" + i, "evidence": "q" + i, "type": typ,
                            "date": date, "source_doc": doc, "chunk_index": 0, "evidence_ok": ok})
        return [c("C001", "a", "t1", date="2009-05-01"), c("C002", "b", "t2", "constraint", "2009-03-01"),
                c("C003", "b", "t3"), c("C004", "a", "t4")]

    def test_merge_blacklist_and_leftovers(self):
        from merge import BlacklistItem, MergedGroup, MergeResult, apply_merge
        result = MergeResult(
            groups=[MergedGroup(member_ids=["C001", "C002", "C001", "C999"], title="M", description="md"),
                    MergedGroup(member_ids=["C004"], title="bad", description="x")],   # C004 is blacklisted below
            blacklist=[BlacklistItem(item_ids=["C004"], title="B", reason="r", category="conflict",
                                     conflicts_with=["C001", "C888"])])
        merged, bl, stats = apply_merge(self.items(), result, "M1.1")
        top = next(r for r in merged if r["title"] == "M")
        self.assertEqual((top["member_ids"], top["sources"], top["mentions"], top["date"], top["id"]),
                         (["C001", "C002"], ["a", "b"], 2, "2009-03-01", "M1.1-01"))
        self.assertEqual(sorted(r["title"] for r in merged), ["M", "t3"])      # merged group + leftover C003
        self.assertEqual((bl[0]["member_ids"], bl[0]["conflicts_with"]), (["C004"], ["C001"]))
        self.assertEqual(stats["ignored_ids"], 2)                          # unknown C999, blacklisted C004 in a group

    def test_blacklist_has_precedence_over_group(self):
        from merge import BlacklistItem, MergedGroup, MergeResult, apply_merge
        result = MergeResult(groups=[MergedGroup(member_ids=["C001", "C002"], title="M", description="md")],
                             blacklist=[BlacklistItem(item_ids=["C002"], title="B", reason="r", category="nonsense")])
        merged, bl, _ = apply_merge(self.items(), result, "M1.1")
        self.assertEqual(next(r for r in merged if r["title"] == "M")["member_ids"], ["C001"])

    def test_second_round_keeps_candidate_ids_and_counts(self):
        from merge import MergedGroup, MergeResult, apply_merge
        first, _, _ = apply_merge(self.items(), MergeResult(
            groups=[MergedGroup(member_ids=["C001", "C002"], title="M", description="md")], blacklist=[]), "M1.1")
        second, _, _ = apply_merge(first, MergeResult(
            groups=[MergedGroup(member_ids=["M1.1-01", "C003"], title="N", description="nd")], blacklist=[]), "M2.1")
        n = next(r for r in second if r["title"] == "N")
        self.assertEqual((n["member_ids"], n["mentions"]), (["C001", "C002", "C003"], 3))


class ClusterTest(unittest.TestCase):
    def test_similar_items_share_a_batch_and_nothing_is_lost(self):
        from merge import cluster_batches, to_item
        topics = ["report missing damaged items shelf", "staff login card swipe credential"]
        items = [to_item({"id": f"C{i:03d}", "title": topics[i % 2] + f" v{i}", "description": topics[i % 2],
                          "evidence": "q", "type": "functional", "date": None, "source_doc": "a",
                          "chunk_index": 0, "evidence_ok": True}) for i in range(8)]
        batches = cluster_batches(items, 4)
        self.assertEqual(sorted(it["id"] for b in batches for it in b), sorted(it["id"] for it in items))
        for b in batches:
            self.assertEqual(len({int(it["id"][1:]) % 2 for it in b}), 1)
