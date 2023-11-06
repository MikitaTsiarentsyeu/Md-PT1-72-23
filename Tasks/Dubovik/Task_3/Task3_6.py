str = str.casefold("My name is Alex eee")
vowels = "aeiou"
str2 = ""
for i in str:
    if i not in vowels:
        str2 = str2 + i
print(str2)


