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

        fakes = {**network.NODES, "extract": fake_extract, "review_completeness": fake_review}
        state = {"documents": [{"id": "a", "text": "x"}, {"id": "b", "text": "x"}],
                 "chunks": [{"doc_id": d, "index": 0, "total": 1, "text": "x"} for d in "ab"]}
        old, network.NODES = network.NODES, fakes
        try:
            result = network.build_graph("extract", "review_gate").invoke(state)
        finally:
            network.NODES = old
        self.assertEqual(result["iteration"], 3)            # initial review + 2 re-extractions
        self.assertEqual([d for d, f in calls["extract"] if f], ["a", "a"])   # b never re-extracted
        self.assertEqual(calls["review"], 6)                # 2 docs x 3 rounds
        self.assertEqual(result["feedback"], {})


class ReviewGateTest(unittest.TestCase):
    def test_ignores_items_with_unverified_quote(self):
        from network import review_gate
        state = {"iteration": 0, "reviews": [{"doc_id": "a", "round": 0, "missing": [
            {"description": "real", "evidence": "q", "quote_ok": True},
            {"description": "invented", "evidence": "z", "quote_ok": False}]}]}
        out = review_gate(state)
        self.assertEqual(out["feedback"], {"a": "- real"})
        self.assertEqual(out["iteration"], 1)
