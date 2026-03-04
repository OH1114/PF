from pathlib import Path
import importlib.util
import unittest


module_path = Path('portfolios/03_business_automation_demo/app/core.py').resolve()
spec = importlib.util.spec_from_file_location('business_core', module_path)
business_core = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(business_core)


class TestBusinessCore(unittest.TestCase):
    def test_rule_summary_contains_rows(self):
        s = business_core.build_rule_based_summary({'rows': 12})
        self.assertIn('12件', s)
        self.assertIn('ルールベース要約', s)

    def test_prompt_contains_summary(self):
        data = {'rows': 3, 'mean': {'h': 2.5}}
        p = business_core.build_report_prompt(data)
        self.assertIn('業務報告向け', p)
        self.assertIn("'rows': 3", p)


if __name__ == '__main__':
    unittest.main()
