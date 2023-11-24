count = 0
new_line = ""
new_f = []


length = int(input('Укажите количество символов в строке (больше 35):'))
while length <= 35:
    print('Количество символов должно быть больше 35!')
    length = int(input('Укажите количество символов в строке:'))
else:
    with open("text.txt", "r") as f:
        text = f.read().split()

    for i in text:
        count += len(i)
        if count >= length:
            new_line += "\n"
            count = len(i)
        elif new_line != "":
            new_line += " "
            count += 1
        new_line += i

    for j in new_line.split("\n"):
        space = length - len(j)
        while space > 0:
            j = j.replace(" ", "  ", space)
            space = length - len(j)
        new_f.append(j + "\n")

    with open("res_text.txt", "w") as f:
        for i in new_f:
            f.write(i)

    print('Результат в файле res_text.txt')