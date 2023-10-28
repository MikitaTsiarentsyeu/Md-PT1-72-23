s = {}
print(type(s), s)

s = set()
print(type(s), s)

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,"test"}
print(s)

s = set("test")
print(s)

l1 = [1,2,3]
l2 = [3,2,1]
print(l1 == l2, set(l1)==set(l2))

# l = [[]]
# set(l) error

s = {1,2,3,4,5}
s.add(1)
s.add("test")
print(s)

s.remove(1)
print(s)
# s.remove(1)
# print(s)
print(s.discard(1))
print(s)

print({1,2,3}.union({3,4,5}))
print({1,2,3}.intersection({3,4,5}))

