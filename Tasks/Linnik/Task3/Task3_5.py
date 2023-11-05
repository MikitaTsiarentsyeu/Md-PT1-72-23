# 5. Write a program that takes a list of strings as input
# returns a list with all strings that have a length greater than 5 characters.
list_of_strings = ['Holla', 'abc', 'Are you ok?', 'aspirin', 'yes', 'no', 'determination']
new_list = []
for i in list_of_strings:
    if len(i) > 5:
        new_list.append(i)
print(new_list)
