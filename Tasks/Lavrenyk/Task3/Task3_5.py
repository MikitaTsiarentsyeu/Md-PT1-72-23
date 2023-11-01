list_of_strings = []
print('Input string. Empty input for end:')

while True:
    user_input = input()
    if not user_input:
        break
    list_of_strings.append(user_input)

print([i for i in list_of_strings if len(i) > 5])