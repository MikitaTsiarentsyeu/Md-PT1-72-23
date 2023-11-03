lst = input('Enter:')
b = lst.split(' ')
c = [int(i) for i in b]
summa = 0
for i in c:
    summa = sum(c)
    srednee = summa/len(c)
print(srednee)
