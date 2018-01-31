from __future__ import print_function
from HTMLParse import HtmlParse
import sys, os, datetime

class Analyzing:
  list_dangerous = list()
  test = HtmlParse
  def __init__(self):
    self.list_dangerous.append("bt_security_potential_insecure_memory_buffer_bounds_restriction_in_call_strcpy_")
    self.list_dangerous.append("bt_security_potential_insecure_memory_buffer_bounds_restriction_in_call_strcat_")
    self.list_dangerous.append("bt_logic_error_out-of-bound_array_access")
    self.list_dangerous.append("bt_logic_error_out-of-bound_access")
    self.list_dangerous.append("bt_general_tainted_data")

    if len(sys.argv) < 2:
      print ("Oops: Missing input direction")
      return
    if os.path.isdir(sys.argv[1]) == 0:
      print ("Oops: Directory does not exist")
      return
    time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    Html = HtmlParse(sys.argv[1] + "/index.html",sys.argv[1] +"/" + time + ".txt", self.list_dangerous)
    Html.analyzingSoureFile()

test = Analyzing()
