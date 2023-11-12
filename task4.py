import os

MAX_LENGTH = int(input('Input the MAX_LENGTH of string (35 and more):'))
if MAX_LENGTH <= 35:
    print('Incorrect input, MAX_LENGTH of string (40 and more)')

with open('text.txt') as f:
    with open('text_str.txt', 'a') as w:
            for string in f.readlines():
                i = MAX_LENGTH
                rows = []

                while True:
                    try:
                        # find an index of the space
                        if str.isspace(string[i]):
                            # append the text to the left of the space
                            rows.append(string[:i])
                            # the index of the end of line
                            string = string[i + 1:]
                            i = MAX_LENGTH

                        else:
                            # go left by step (-1)
                            i -= 1
                            continue
                    except:
                        # for the last line
                        rows.append(string.strip('\n'))
                        break

                while True:
                    #check the length of i - line and create the set of incomplete lines
                    l = {len(i) for i in rows[:-1]}
                    # in case of point
                    if len(l) == 1:
                        w.write('\n'.join(rows))
                        w.write('\n')
                        break

                    # list oh indexes of incomplete lines
                    l_num = [i for i in range(len(rows[:-1])) if len(rows[i]) < MAX_LENGTH]
                    for i in l_num:
                        row_i = len(rows[i])
                        # indexes of spices
                        spice = rows[i].split()
                        s = 0
                        while row_i < MAX_LENGTH:
                            try:
                                spice[s + 1]
                                spice[s] = spice[s] + ' '
                                s += 1
                                row_i += 1
                            except:
                                s = 0
                        rows[i] = ' '.join(spice)

    print('The result is at the file \'text_str.txt\'')