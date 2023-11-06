lst = input('Enter:')
b = lst.split(' ')
rest = []

for i in b:
    if len(i) > 5:
        rest.append(i)
print(rest)
