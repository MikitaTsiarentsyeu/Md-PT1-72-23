x = range(100)
print(type(x))

x = map(lambda x: x, x)
print(type(x))

def bad_generator():
    yield 1
    yield 2
    yield 3

x = bad_generator()
print(x, type(x))

# print(list(x))
for i in x:
    print(i)

def infinity():
    i = 0
    while True:
        i += 1
        yield i

x = infinity()

# print(list(x))

# for i in infinity():
#     print(i)

i = iter(x)
print(next(i))
print(next(i))
print(next(i))

gen1 = bad_generator()
gen2 = bad_generator()

for i in gen1:
    print(i)

for i in gen2:
    print(i)

print("the end")

for i in gen1:
    print(i)



def even_cubes(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i**3

print(list(even_cubes(10)))


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1
        if count == n:
            break
        a, b = b, a+b

# def fibonacci(n):
#     res = []
#     a, b = 0, 1
#     count = 0
#     while True:
#         res.append(a)
#         count += 1
#         if count == n:
#             break
#         a, b = b, a+b

#     return res

print(list(fibonacci(10)))


l = [1,2,3, [4,5,6, [7,8,9, [0]]]]

# def flatten(l, res=[]):
#     for i in l:
#         if isinstance(i, int):
#             res.append(i)
#         else:
#             flatten(i, res)
    
#     return res

def flatten(l):
    for i in l:
        if isinstance(i, int):
            yield i
        else:
            yield from flatten(i)

print(list(flatten(l)))

print([x*x for x in range(10)])
sq = (x*x for x in range(10))

# print(list(sq))
for i in sq:
    print(i)