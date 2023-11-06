# the program takes any string and returns the number of vowels in the string.

text = input('Input any words: ').lower()
alphabet = 'aeiouy'
counter = 0
for i in range(len(text)):
    if text[i] in alphabet:
        counter += 1
print(f'The number of vowels in the string = {counter}')
    