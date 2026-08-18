import importlib.util,json,tempfile,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/event_shotlist_planner.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_result(self):
  data=json.loads("[{\"stage\":\"церемония\",\"shot\":\"общий план\",\"done\":false},{\"stage\":\"церемония\",\"shot\":\"деталь\",\"done\":true}]"); result=x.run(data,'2026-08-18',7); self.assertTrue(result is not None)
if __name__=='__main__':unittest.main()
