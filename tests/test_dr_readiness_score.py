import importlib.util, unittest
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/"tools/dr_readiness_score.py"; spec=importlib.util.spec_from_file_location("score",SCRIPT); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
class Tests(unittest.TestCase):
 def test_full_score(self): self.assertEqual(module.score({"controls":{name:2 for name in module.CONTROLS}})["score"],20)
 def test_invalid_value(self): self.assertTrue(module.score({"controls":{name:3 for name in module.CONTROLS}})["errors"])
if __name__=="__main__": unittest.main()
