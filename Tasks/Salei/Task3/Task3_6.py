user_input = "Write a program that takes a string as input and returns the string"
l = list(user_input)
vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
con_list = []

for i in l:
    if i not in vowels_list:
        con_list.append(i)

print("".join(con_list))