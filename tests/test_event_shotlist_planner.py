import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/event_shotlist_planner.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_workflow(self):
  r=x.run([{'stage':'церемония','shot':'общий','done':False},{'stage':'церемония','shot':'деталь','done':True}],'2026-08-18',7); self.assertTrue(r=={'церемония':['общий']})
if __name__=='__main__':unittest.main()
