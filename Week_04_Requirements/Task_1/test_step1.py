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
