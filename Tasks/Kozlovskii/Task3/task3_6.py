A = input('')
new_string = ''
for i in A:
    if i.lower() not in 'aeiouy':
        new_string += i
print(new_string)