a = input('Enter:')
b = a.split(' ')
# print(b, type(b))
c = [int(i) for i in b]
# print(c,type(c))

lst = []

for i in c:
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            lst.append(i)

# print(lst)

for a in range(len(lst)-1):
    max_i = a
    for i in range(a+1, len(lst)):
        if lst[i]>lst[max_i]:
            max_i = i
    lst[max_i], lst[a] = lst[a], lst[max_i]
print(lst[0])


