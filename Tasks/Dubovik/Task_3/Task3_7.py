str = ("My name is Alex eee")
str2 = ""
for i in str:
    if i.isupper():
        str2 = str2 + i.casefold()
    else:
        str2 = str2 + i.upper()
print(str2)