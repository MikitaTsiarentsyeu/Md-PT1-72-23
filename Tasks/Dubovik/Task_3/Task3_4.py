list= [1,2,3,4,5,35]
max = list[0]
print(max)
secondmax = list[1]
for i in list:
    if i > max:
        max = i
for i in list:
    if i > secondmax and i != max:
        secondmax = i

print(max , secondmax)