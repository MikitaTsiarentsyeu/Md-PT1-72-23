# while True:
#     print("it's true")
#     print("infinity!")

l = [1,2,3,4,5]

# i = 0
# while i<len(l):
#     print(l[i])
#     i+=1

for element in l:
    print(element)

for element in "test str":
    print(element)

for element in set("test str"):
    print(element)

d = {1:"one", 2:"two", 3:"three"}

for key in d:
    print(key, d[key]) 

for item in d.items():
    print(item) 

# for keys in d.keys():
#     print(keys) 

for value in d.values():
    print(value) 

x = range(10)
print(type(x))

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

s = "very long test str"
for i in range(len(s)):
    print(s[i])

for i, e in enumerate(s):
    print(i, e)

l = [[1,2,3], (4,5,6), {7,8,9}]

for i in l:
    print(i)
    for j in i:
        print(j)


while True:
    break

my_break = False

for i in range(10):
    if i > 15:
        my_break = True
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("it's else")

s = "test str"
i = 0

while True:
    if i == len(s):
        break
    if s[i] == ' ':
        i+=1
        continue
    print(s[i])
    i+=1
else:
    print("it's else")


