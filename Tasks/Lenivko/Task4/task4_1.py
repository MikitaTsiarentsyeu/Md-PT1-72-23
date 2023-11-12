# validation.
while True:
    lenght = input('Enter the maximum number of characters per line. Your value must be greater than 35: ')
    if lenght.isdigit() == False:
        print('Incorrect input. Your value must be a digit')
        continue
    if int(lenght) <= 35:
        print('Incorrect input.Your value must be greater than 35')
        continue
    lenght = int(lenght)
    break
print("Ok.Let's transform your text")

# formating
with open('text.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()
    line = ''
    with open('formated.txt', 'w', encoding='utf-8') as new_file:
        for word in words:
            pre_line = line
            line = word if not line else f'{line} {word}'
            if len(line) > lenght - 1:
                missing_char = (lenght - 1) - len(pre_line)
                spaces = pre_line.count(' ')
                all = (missing_char//spaces) + 1
                counter = 0
                if missing_char == 0:
                    pre_line
                elif missing_char < spaces:
                    counter = missing_char
                elif missing_char >= spaces:
                    all -= 1
                    counter = spaces
                spaces_to_replace = ' ' + ' ' * all
                pre_line = pre_line.replace(' ', spaces_to_replace, counter)

                new_file.write(f'{pre_line}\n')
                line = word
            else:
                continue
        print('The file with formated text were created as formated.txt')