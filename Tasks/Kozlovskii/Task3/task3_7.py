text = input()
new_text = ''
for i in text:
    if i.islower():
        new_text += i.upper()
    else:
        new_text += i.lower()
print(new_text)
