# A program takes a list of strings as input and returns a list with all strings that have a length greater than 5 characters.


string_list = []
for _ in range(5):
    text = input('Enter any string five times: ')
    string_list.append(text)

result_list = []
for i in range(len(string_list)):
    if len(string_list[i]) > 5:
        result_list.append(string_list[i])
print(result_list)