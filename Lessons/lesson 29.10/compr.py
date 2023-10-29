# l = []
# for i in range(1,11):
#     if i % 2 == 0:
#         if i % 5 == 0:
#             l.append(i)

l = [i*i for i in range(1,101) if i % 2 == 0 if i % 5 == 0]

print(l)

l = [chr(i) for i in range(1,101) if i % 2 == 0 if i % 5 == 0]
print(l)

l1 = [1,2,3]
l2 = "abc"

# for i in l1:
#     for j in l2:
#         print(f"{i}-{j}")

l = [f"{i}-{j}" for i in l1 for j in l2]
print(l)

s = {chr(i) for i in range(1,101) if i % 2 == 0 if i % 5 == 0}
print(s)

d = {i:chr(i) for i in range(1,101) if i % 2 == 0 if i % 5 == 0}
print(d)

t = (chr(i) for i in range(1,101) if i % 2 == 0 if i % 5 == 0)
print(t)

for i in t:
    print(i)