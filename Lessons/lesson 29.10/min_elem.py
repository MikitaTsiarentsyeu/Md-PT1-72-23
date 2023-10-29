l = [3,5,67,87,5,3,2,3,3,5,7,9,7,90,-1]

target = 3
for i in range(len(l)): #every position
    if l[i] == target:
        print("found it! - ", i)

for i in range(len(l)): #the first position
    if l[i] == target:
        print("found it! - ", i)
        break

pos = -1
for i in range(len(l)):
    if l[i] == target:
        # print("found it! - ", i)
        pos = i
if pos >= 0:
    print("found it! - ", pos)

# for i in l[::-1]:
    # print(i)

# for i in range(len(l)-1, -1, -1):
#     print(i)

#min elem


min_i = 0
for i in range(1, len(l)):
    if l[i]<l[min_i]:
        min_i = i
print("min elem - ", min_i, l[min_i])

# print(sorted(l)[0])

is_sorted = True
for i in range(len(i)-1):
    if l[i] > l[i+1]:
        is_sorted = False
        break
