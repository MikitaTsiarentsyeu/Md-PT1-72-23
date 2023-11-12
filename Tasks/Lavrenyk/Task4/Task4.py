import os


def val():
    while True:
        try:
            symbols = int(input('Input number of characters per line (greater than 35): '))
            if symbols <= 35:
                print('Incorrect input, it must be greater than 35 characters')
                continue
            else:
                return symbols
        except ValueError:
            print('Incorrect input')
            continue


def main():
    symbols = val()  # Validation

    with open('text.txt') as f:  # Open file text.txt for reading
        with open('format_text.txt', 'a') as w:  # Create new file for write info
            for line in f.readlines():  # Reading lines from file text.txt
                parts = []  # Creating an empty list to add lines of the desired or less length
                i = symbols

                while True:
                    try:
                        if line[i] == ' ':  # If the line symbol under the index i is equal to a space,
                            parts.append(line[:i])  # then everything that is before it is added to the list
                            line = line[i + 1:]  # and the line is overwritten without this section
                            i = symbols
                        elif line[i] == '\n':
                            raise IndexError
                        else:
                            i -= 1
                            continue
                    except IndexError:
                        parts.append(line.strip('\n'))  # Appending last line without \n
                        break

                while True:
                    lengths = {len(i) for i in parts[:-1]}  # Creating set() to check the number of unsuitable lines
                    lengths_ind = [i for i in range(len(parts[:-1])) if len(parts[i]) != symbols]  # Find indexes of this lines
                    if len(lengths) == 1:
                        w.write('\n'.join(parts))
                        w.write('\n')
                        break

                    for i in lengths_ind:
                        n_chars = len(parts[i])
                        part = parts[i].split()
                        k = 0
                        while n_chars != symbols:
                            try:
                                part[k + 1]  # If part[k + 1] not exist then catching an exception and going through the loops again
                                part[k] = part[k] + ' '
                                k += 1
                                n_chars += 1
                            except Exception:
                                k = 0
                        parts[i] = ' '.join(part)


if __name__ == '__main__':
    if os.path.isfile('format_text.txt'):  # If file already exist then remove it
        os.remove('format_text.txt')
    main()
    print('The task is done.\nYou can check the results at the file \'format_text.txt\'')
