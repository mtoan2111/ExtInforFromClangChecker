from __future__ import print_function
from HTMLParse import HtmlParse

list_dangerous = []

list_dangerous.append("bt_security_potential_insecure_memory_buffer_bounds_restriction_in_call_strcpy_")
list_dangerous.append("bt_security_potential_insecure_memory_buffer_bounds_restriction_in_call_strcat_")
list_dangerous.append("bt_logic_error_out-of-bound_array_access")


test = HtmlParse("/home/toannm/report/02_11/less/ffmpeg/2017-11-03-152218-9185-1/index.html","/home/toannm/dangerous/readelf.txt", list_dangerous)
test.analyzingSoureFile()
