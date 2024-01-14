second = "ooops"

# import second
# from second import test_list as tst_lst, test_str as tst_str, print_list, print_str, change_list
from second import *

test_list[0] = 1.1111111

print(test_list)
print_list()

change_list()

print(test_list)
print_list()

# scnd.__dict__["test_str"] = "test str from the second file"

test_str = "test"

# scnd.__dict__["test_str"] = "test"

print(test_str)
print_str()