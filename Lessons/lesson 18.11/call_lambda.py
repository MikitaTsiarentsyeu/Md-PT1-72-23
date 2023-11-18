import threading
import time

def test_func():
    print("this is only a test")

def call_a_func(f):
    f()

call_a_func(test_func)

l = [3,6,3,2]
print(sorted(l))

s = "A a B b"
print(sorted(s.split(), key=str.upper))


def apply(l, f):
    for i in l:
        f(i)

apply([1,2,3,4,5], print)

def print_inline(i):
    print(i, end=' ', flush=True)

apply([1,2,3,4,5], print_inline)

# print("before sleep")
# time.sleep(3)
# print("after sleep")

# print('')

def timer(f, t):
    time.sleep(t)
    f()

# timer(test_func, 3)
# threading.Timer(3, test_func).start()
# for i in range(70000):
#     print(i, end=' ', flush=True)

def sum(a, b):
    return a+b

sum = lambda a, b: a+b

# lambda a, b, c: print(a, b, c, sep=' ')

print(sum(2, 3))

d = {1:"one", 2:"two", 3:"three"}

def get_value(k):
    return d[k]

print(sorted(d, key=lambda x: d[x]))

l = [(2, "two"), (1, "one"), (3, "three")]
print(sorted(l, key=lambda x: x[1]))