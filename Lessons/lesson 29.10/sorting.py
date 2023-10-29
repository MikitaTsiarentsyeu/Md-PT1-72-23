l = [3,5,67,9,7,90,-1]

# print(sorted(l), l)

# l.sort()
# print(l)

# print('4' < '8')
# print('a' < 'A')

# count = 0
# for j in range(len(l)-1):
#     for i in range(len(l)-j-1):
#         count+=1
#         if l[i]>l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
#     print(l)

# print(count)

for j in range(len(l)-1):
    min_i = j
    for i in range(j+1, len(l)):
        if l[i]<l[min_i]:
            min_i = i
    l[min_i], l[j] = l[j], l[min_i]
    print(l)