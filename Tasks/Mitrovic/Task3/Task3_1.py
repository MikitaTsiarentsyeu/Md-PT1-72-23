my_str = 'I would like to go to the cinema on Saturday.'
vowels_l = []
for i in my_str:
    if i in 'AEIOUYaeiouy':
        vowels_l.append(i)
print('The number of vowels in my string:', len(vowels_l))
