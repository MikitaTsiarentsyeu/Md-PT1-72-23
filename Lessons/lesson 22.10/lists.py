l = [1,2,3,4,5.0,"test"]

print(len(l))

print(type(l), l)

l = []

print(len(l))

l = [1,2,3,4,5.0,"test"]

print(l[0],l[1], l[2],l[3],l[4], l[5])
print(l[-1],l[-2],l[-3], l[-4],l[-5])

print(l[0:3])
print(l[0:1])
print(l)
print(l[1:-2])
print(l[1:-2:2])

reverse = l[::-1]
print(reverse)

# l[110000] index out of range

l[0] = 1.0
print(l)

l.append("new elem")
print(l)

l.extend("new elem")
print(l)

print([1,2,3]+[4,5,6]*3)

l.insert(0, "new first elem")
print(l)

print(l.pop())
print(l)

print(5.1 in l)

l.remove('e')
print(l)
l.remove('e')
print(l)

del l[0]
print(l)

del l[0:5]
print(l)

# del l
# print(l)

l.clear()
print(l)

l1 = l2 = []
print(l1, l2)
print(l1 == l2)
print([] == [])
print(id(l1))
print(id(l2))
print(id(l1) == id(l2))
print(l1 is l2)

l1.append("new elem")
print(l2, l1)

l = []
l.append(l)
print(l)

l.append("test")

print(l[0][0][0][0])