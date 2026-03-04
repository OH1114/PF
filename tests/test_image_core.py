from pathlib import Path
import importlib.util
import unittest


module_path = Path('portfolios/02_image_inspection_demo/app/core.py').resolve()
spec = importlib.util.spec_from_file_location('image_core', module_path)
image_core = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(image_core)


class TestImageCore(unittest.TestCase):
    def test_score_from_values(self):
        vals = [[0, 100], [60, 30]]
        score, bright, total = image_core.simple_defect_score_from_values(vals, threshold=50)
        self.assertEqual(bright, 2)
        self.assertEqual(total, 4)
        self.assertAlmostEqual(score, 50.0)

    def test_empty_values(self):
        score, bright, total = image_core.simple_defect_score_from_values([], threshold=50)
        self.assertEqual((score, bright, total), (0.0, 0, 0))

    def test_judge(self):
        self.assertEqual(image_core.judge_defect(5.0, 4.0), '要確認')
        self.assertEqual(image_core.judge_defect(2.0, 4.0), '許容範囲')


if __name__ == '__main__':
    unittest.main()
