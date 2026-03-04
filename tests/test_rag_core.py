import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path('portfolios/01_rag_local_demo').resolve()))

from app.rag_core import Chunk, answer_with_local_template, load_chunks, retrieve, score


class TestRagCore(unittest.TestCase):
    def test_score_overlap(self):
        self.assertGreater(score('api key policy', 'api key must be hidden'), 0)

    def test_retrieve_returns_relevant_or_fallback(self):
        chunks = [
            Chunk(source='a.txt', text='alpha beta security'),
            Chunk(source='b.txt', text='image defect detection'),
        ]
        hits = retrieve('security rule', chunks)
        self.assertGreaterEqual(len(hits), 1)
        self.assertEqual(hits[0].source, 'a.txt')

    def test_answer_template_contains_citation(self):
        hits = [Chunk(source='doc.txt', text='SLA is 24h')]
        ans = answer_with_local_template('SLAは？', hits)
        self.assertIn('[doc.txt]', ans)

    def test_load_chunks_from_data(self):
        data_dir = Path('portfolios/01_rag_local_demo/data')
        chunks = load_chunks(data_dir)
        self.assertGreaterEqual(len(chunks), 1)


if __name__ == '__main__':
    unittest.main()
