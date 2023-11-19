from functools import reduce

lambda a, b: a*b

def apply(l, f):
    for i in l:
        f(i)

# apply([1,2,3,4,5], lambda x: print(x*x))

l = [1,2,3,4,5,6,7,8,9,10]

map_res = map(lambda x: ord(x), map(lambda x: chr(x*x), l))
# for i in map_res:
#     print(i)
print(list(map_res))

print(list(filter(lambda x: x%2==0, l)))

print(list(map(lambda x: chr(x*x), filter(lambda x: x%2==0, l))))

print(reduce(lambda a, b: a+b, [1,2,3,4,5]))

print(reduce(lambda a, b: f"{a}-{b}", [1,2,3,4,5]))

print(reduce(lambda a, b: a if a > b else b, [1,2,33,4,5]))