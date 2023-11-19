import random
import math

def do_twice(f):
    def wrapper():
        print("The first call of the function")
        f()
        print("The second call of the function")
        f()
    return wrapper


def test_func():
    print("this is only a test")


# twice_test_func = do_twice(test_func)
# twice_test_func()

test_func = do_twice(test_func)
test_func()

def comment_process(target_func):
    def wrapper(a, b=None):
        print(f"The execution of the {target_func.__name__} is started, the parameters are {a}, {b}")
        result = target_func(a, b)
        print(f"The result is {result}")
        return result
    return wrapper

def generate(a=1, b=10):
    return random.randint(a, b)

def test_str(a=1, b=1000):
    return chr(random.randint(a, b))

print(generate(1, 10))
print(generate(1, 10))
print(generate(1, 10))

generate = comment_process(generate)

print(generate(1, 10))
print(generate(1, 10))
print(generate(1, 10))

test_str = comment_process(test_str)

print(test_str(1, 1000))
print(test_str(1, 1000))
print(test_str(1, 1000))

# print = comment_process(print)
# print(5, "test")

pow = comment_process(pow)
pow(2, 3)

def check_password(func):
    password = "P@$$w(0)rd"
    def wrapper(a, b):
        inpt = input("Please provide a password:\n")
        if password == inpt:
            func(a, b)
        else:
            print("Access denied!")
    return wrapper

@check_password
@comment_process
def sum(a, b):
    return a+b

# sum = comment_process(sum)

sum(2, 3)