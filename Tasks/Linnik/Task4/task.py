# 3. Format the text taking into account the maximum number of characters,
# but if a word does not fit entirely on a line,
# it should be moved to the next one, and the spacing between words should be evenly increased

# if '\n' in chunk:
    #     return n, line
    # Если /n в середине, то следующей строке будет больше символов

# def check_line(n, line):
#     # next_symbol = t.read(1)
#     # if next_symbol == ' ' or next_symbol == '\n':
#     #     return n, line + '\n'
#     return n, line + '\n'


number = 0
while number <= 35:
    number = int(input('Enter your number of characters per line and this number must be greater than 35: '))

with open('text.txt', 'r', encoding='utf8') as t:
    with open('rewrited_text.txt', 'w', encoding='utf8') as rewrited_t:
        next_symbol = True
        while next_symbol:
            chunk = t.read(number)
            next_symbol = t.read(1)
            if chunk == '':
                break

            if len(chunk) < number:
                rewrited_t.write(chunk)
            elif '\n' in chunk[1:number-2]:
                ind = chunk.index('\n')
                chunk = chunk[:ind]
                lost_symbols = number - len(chunk)
                #//

            elif next_symbol in (' ', '\n'):
                rewrited_t.write(chunk+'\n')
            elif chunk[number-1] in (' ', '\n'):
                chunk = chunk.replace(' ', '  ', 1)  # --> 'text  text '
                if chunk[number-1] == ' ':
                    chunk = chunk[:number-1]  # --> 'text  text'
                    rewrited_t.write(chunk + '\n')
                elif chunk[number-1] == '\n':
                    rewrited_t.write(chunk)
            elif chunk[0] in (' ', '\n'):
                chunk = chunk[1:]
                chunk = chunk.replace(' ', '  ', 1)
                rewrited_t.write(chunk + '\n')
            # else:

            t.seek(t.tell()-1)
print('We did it!')
