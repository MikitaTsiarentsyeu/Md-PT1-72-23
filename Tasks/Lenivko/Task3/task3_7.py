# A program takes a string and returns the string with all capital letters converted to lowercase and vice versa.

# As we learn loops we can solve this task by doing next steps:

# text = input().split()
# result_list = []
# for i in range(len(text)):
#     for j in range(len(text[i])):
#         if text[i][j] == text[i][j].upper():
#             result_list.append(text[i][j].lower())
#         else:
#             result_list.append(text[i][j].upper())
# print(''.join(result_list))

# but:
string = input()
print(string.swapcase())