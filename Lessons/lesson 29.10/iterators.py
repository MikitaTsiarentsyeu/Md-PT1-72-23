s = set("test str")
print(s)

for i in s:
    print(i, hash(i))

# s[0] error

s_iter = iter(s)
print(s_iter, type(s_iter))

l_iter = iter([1,2,3,4,5])
print(l_iter, type(l_iter))

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

# int("kyhgh")
# list(54545) error

s = "test"
for i in s:
    for j in s:
        print(i, j)

print("after the cycle", i, j)

for i in range(5):
    i+=1

print(i)

l = [1,2,3,4,5]
for i in l:
    if len(l) >= 100:
        break
    if i % 2 == 0:
        l.append(i*2)
        print(l)
    
for i in l:
    print(i)
    print(l.pop())
print(l)