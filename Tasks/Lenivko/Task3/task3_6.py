# a program takes a string as input and returns the string with all vowels removed.


text = input('Enter your string here: ')
alphabet = 'aeiouy'
result_list = []
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] not in alphabet:
            result_list.append(text[i])
result = ''.join(result_list)
print(result)