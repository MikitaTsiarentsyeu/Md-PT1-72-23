my_str = 'I like to move it'
my_str_low = my_str.lower()
print(my_str_low)
vowels = []
for i in my_str_low:
    if i in 'bcdfhqjklmnpqrstvwxz':
        vowels.append(i)
number_vowels = len(vowels)
print(f'The number of vowels is {number_vowels}.')
