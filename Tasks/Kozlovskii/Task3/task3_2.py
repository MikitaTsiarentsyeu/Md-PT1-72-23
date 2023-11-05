lst = input('Enter:')
b = lst.split(' ')
c = [int(i) for i in b]
rest = 0

for i in c:
    if i % 2 == 0:
        rest += i
print(rest)








