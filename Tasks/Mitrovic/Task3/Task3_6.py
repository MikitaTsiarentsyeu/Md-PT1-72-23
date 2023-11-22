my_str = 'I would like to go to the cinema on Saturday and I would like to go to London on Sunday.'
my_new_str = ''
for i in my_str:
    if i not in 'AEIOUYaeiouy':
        my_new_str += i
        my_new_str += ' '
print(my_new_str)
