t = (1,2,3,4,5,"test")

print(len(t), t, type(t))

# t = (1,)
# print(type(t))

print(t[0], t[-1], t[0:3], t[::-1])

print((1,2,3)+(0,)*10)

# t[0] = 1 error

del t

print(tuple(list("test str")))

t = (1,2,3,4,5)
t = list(t)
t.append("test")
t = tuple(t)
print(t)

t = ()
print(type(t))