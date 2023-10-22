d = {}
print(d, type(d), len(d))

d = {1:"one", 2:"two", 3:"three"}

print(d)

print(d[2])

d["test"] = [1,2,3,4,5]
print(d)

print(list(d.items())[0])
print(list(d.keys())[0])
print(list(d.values())[0])

d["test"] = "test"
print(d)

d["test"] = 9
print(d)

