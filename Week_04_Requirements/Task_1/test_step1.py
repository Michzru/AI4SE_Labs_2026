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


class PriorityTest(unittest.TestCase):
    DOC = ("OE-1: The system must run on Linux\n      or Solaris.\n      [* High Priority]\n\n"
           "OE-4: Support Firefox.\n      [* Medium Priority]\n\nOE-9: Nothing tagged here.\n")

    def index(self):
        from textutil import squash_with_positions
        return {"d": (*squash_with_positions(self.DOC), self.DOC)}

    def req(self, quote, sources=("d",), mentions=1):
        return {"evidence": [{"source_doc": "d", "quote": quote, "verified": True}],
                "sources": list(sources), "mentions": mentions}

    def test_stated_priority_is_read_next_to_the_quote(self):
        from priority import stated_priority
        idx = self.index()
        self.assertEqual(stated_priority(self.req("must run on Linux or Solaris"), idx), "Must")
        self.assertEqual(stated_priority(self.req("Support Firefox."), idx), "Should")
        self.assertIsNone(stated_priority(self.req("Nothing tagged here."), idx))
        self.assertIsNone(stated_priority(self.req("a quote that is not in the document"), idx))

    def test_baseline_from_signals(self):
        from priority import baseline
        self.assertEqual(baseline({"stated": None, "source_count": 1, "mentions": 9, "strong_words": []})[0], "Could")
        self.assertEqual(baseline({"stated": None, "source_count": 2, "mentions": 2, "strong_words": []})[0], "Should")
        self.assertEqual(baseline({"stated": None, "source_count": 3, "mentions": 3, "strong_words": ["must"]})[0], "Must")
        self.assertEqual(baseline({"stated": "Should", "source_count": 5, "mentions": 5, "strong_words": ["must"]})[0], "Should")

    def test_model_cannot_move_more_than_one_level_or_touch_stated(self):
        from priority import clamp
        self.assertEqual(clamp("Could", "Must", locked=False), "Should")
        self.assertEqual(clamp("Must", "Could", locked=False), "Should")
        self.assertEqual(clamp("Should", "Must", locked=False), "Must")
        self.assertEqual(clamp("Should", "Must", locked=True), "Should")
        self.assertEqual(clamp("Should", None, locked=False), "Should")
        self.assertEqual(clamp("Should", "Urgent!", locked=False), "Should")

    def test_prioritize_node_falls_back_to_baseline_on_missing_answers(self):
        import network
        reqs = [{"title": "a", "description": "d", "type": "functional", "date": None, "member_ids": ["C1"],
                 "mentions": 1, "sources": ["d"],
                 "evidence": [{"source_doc": "d", "quote": "Support Firefox.", "verified": True}]},
                {"title": "b", "description": "d", "type": "functional", "date": None, "member_ids": ["C2"],
                 "mentions": 1, "sources": ["d"],
                 "evidence": [{"source_doc": "d", "quote": "Nothing tagged here.", "verified": True}]}]
        old = network.prioritize_batch
        network.prioritize_batch = lambda batch: {}      # the model answers nothing at all
        try:
            out = network.prioritize({"documents": [{"id": "d", "text": self.DOC}], "requirements": reqs})
        finally:
            network.prioritize_batch = old
        self.assertEqual([(r["priority"], r["priority_source"]) for r in out["requirements"]],
                         [("Should", "stated"), ("Could", "signals")])


class RenderTest(unittest.TestCase):
    def data(self):
        def req(title, prio, date, members):
            return {"title": title, "description": "desc " + title, "type": "functional", "date": date,
                    "member_ids": members, "mentions": 1, "sources": ["a.txt"], "priority": prio,
                    "priority_basis": "Because.", "priority_source": "signals",
                    "evidence": [{"source_doc": "a.txt", "quote": "q |\n" + title, "verified": True}]}
        reqs = [req("Low", "Could", "2009-01-01", ["C1"]), req("Late", "Must", "2009-05-01", ["C2"]),
                req("Early", "Must", "2009-02-01", ["C3"]), req("Undated", "Must", None, ["C4"])]
        bl = [{"title": "Bad", "reason": "r", "category": "conflict", "conflicts_with": ["C3", "C9"],
               "member_ids": ["C5"], "sources": ["b.txt"], "evidence": []}]
        return reqs, bl

    def test_ids_follow_priority_then_date_and_conflicts_are_mapped(self):
        from render import assign_ids
        reqs, bl = assign_ids(*self.data())
        self.assertEqual([(r["id"], r["title"]) for r in reqs],
                         [("REQ-001", "Early"), ("REQ-002", "Late"), ("REQ-003", "Undated"), ("REQ-004", "Low")])
        self.assertEqual((bl[0]["id"], bl[0]["conflicts_with"]), ("BL-001", ["REQ-001"]))   # C9 unknown -> dropped

    def test_document_passes_self_check_and_check_detects_problems(self):
        from render import assign_ids, check_document, render_markdown
        reqs, bl = assign_ids(*self.data())
        md = render_markdown(reqs, bl, ["a.txt", "b.txt"])
        self.assertEqual(check_document(md, reqs, bl), [])
        self.assertIn("## Priority scale", md)
        self.assertIn("### BL-001 - Bad", md)
        broken = [{**reqs[0], "priority": "Urgent", "sources": []}] + reqs[1:]
        problems = check_document(md, broken, bl)
        self.assertTrue(any("OS6" in p for p in problems) and any("OS4" in p for p in problems))


class ElaborationTest(unittest.TestCase):
    DOC = ("Intro paragraph about nothing.\n\nStaff need a report of all items that went missing during\n"
           "transit, because 3 branches lost items last year.\n\nUnrelated closing remarks.\n")

    def req(self, quote="all items that went missing during transit", sources=("d",)):
        return {"title": "Report Missing Items", "description": "The system must report missing items.",
                "type": "functional", "date": None, "member_ids": ["C1"], "mentions": 1, "sources": list(sources),
                "evidence": [{"source_doc": "d", "quote": quote, "verified": True}]}

    def test_retrieval_anchors_on_quote_and_falls_back_to_similarity(self):
        from context import index_documents, retrieve
        docs = index_documents([{"id": "d", "text": self.DOC}])
        by_quote = retrieve(self.req(), docs)
        self.assertEqual(by_quote[0]["how"], "quote")
        self.assertIn("3 branches lost items", by_quote[0]["text"])
        lost = retrieve(self.req(quote="a quote the model made up"), docs)       # not found -> similarity
        self.assertEqual(lost[0]["how"], "similarity")
        self.assertIn("went missing", lost[0]["text"])

    def test_guards(self):
        from elaborate import name_ok, paragraph_ok
        grounding = "3 branches lost items"
        good = "The system must report items that went missing in transit. " * 3
        self.assertTrue(paragraph_ok(good + "Three of 3 branches asked.", grounding))
        self.assertFalse(paragraph_ok(good + "A total of 47 branches asked.", grounding))   # invented number
        self.assertFalse(paragraph_ok("Too short.", grounding))
        self.assertTrue(name_ok("Report Missing Items"))
        self.assertFalse(name_ok("Report."))
        self.assertFalse(name_ok("A very long name that goes on and on and on and on and on forever"))

    def test_nodes_fall_back_when_the_model_misbehaves(self):
        import network
        reqs = [{**self.req(), "contexts": [{"source_doc": "d", "text": "3 branches lost items", "how": "quote"}]}
                for _ in range(2)]
        good = "The system must report items that went missing in transit. " * 3
        old = network.write_batch, network.name_batch
        network.write_batch = lambda batch: {"P001": good, "P002": good + "Also 99 libraries."}
        network.name_batch = lambda batch: {"P001": "Report Missing Transit Items", "P002": "x"}
        try:
            out = network.write_paragraphs({"requirements": reqs})["requirements"]
            self.assertEqual([r["paragraph_source"] for r in out], ["model", "merge_summary"])
            self.assertEqual(out[1]["description"], "The system must report missing items.")
            named = network.name_requirements({"requirements": out})["requirements"]
        finally:
            network.write_batch, network.name_batch = old
        self.assertEqual([r["title"] for r in named], ["Report Missing Transit Items", "Report Missing Items"])
