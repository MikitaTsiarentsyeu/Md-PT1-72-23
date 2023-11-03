list= [1,2,3,4,5,6,7,8,9,10,11]
list2 = []
max = list[0]
for i in list:
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            list2.append(i)
for i in list2:
    if i > max:
        max = i
print(max)










