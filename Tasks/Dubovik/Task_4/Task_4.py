with open("text.txt") as file:
    list = []
    text = file.readlines()

for char in text:
    text = char.strip().split()
    list += [text]

new_text = ""
new_string = ""
param = input("Please enter maximum number of characters per line // must be greater than 35: ")

while True:
    if int(param) <= 35:
        print("Incorrect value, input again")
        continue
    if not param.isdigit():
        print("Incorrect value, input again")
        continue
    break

for words in list:
    for char in words:
        if not new_string:
            new_string += char
            continue
        param = int(param)
        if len(new_string) + len(char) > param - 1:
            count = 1
            while len(new_string) != param:
                missing_space = param - len(new_string)
                new_string = new_string.replace(" " * count, " " + " " * count, missing_space)
                count += 1
            new_text += new_string + "\n"
            new_string = char
        elif len(new_string) + len(char) == param - 1:
            new_text += new_string + " " + char + "\n"
            new_string = ""
        else:
            new_string += " " + char

    if new_string:
        new_text += new_string + "\n"
        new_string = ""

with open("new_text.txt", "w") as f:
    f.write(new_text)

print(f"new_text.txt with {param} characters has been created")