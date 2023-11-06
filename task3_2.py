user_input = input('Enter your numbers through spaces: ')
l = [int(i) for i in user_input.split()]
print (l)
even = 0
for i in l:
    if i % 2 == 0:
        even += i
print(even)