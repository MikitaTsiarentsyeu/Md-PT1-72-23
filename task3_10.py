
a = list(map(int, input('Enter your numbers through spaces: ').split()))
lst = []
i = 1
for i in a:
    if i % 2 ==0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 9 == 0:
        continue
    else:
        lst.append(i)
#print (lst)
print (max(lst))