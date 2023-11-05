
def my_sum(a, b):
    res = a+b
    return res

print(my_sum(2, 3))
print(my_sum(0, 3))

def level_1():
    print("level 1 is working")
    level_2()

# level_1()

def level_2():
    print("level 2 is working")

level_1()

print(level_1, id(level_1))

# sign = "+"
# if sign == "+":
#     def oper(a, b):
#         return a+b
# elif sign == "-":
#     def oper(a, b):
#         return a-b
# elif sign == "*":
#     def oper(a, b):
#         return a*b
# elif sign == "/":
#     def oper(a, b):
#         return a/b
    
# print(oper(2, 3))

def oper(sign, a, b):
    if sign == "+":
        return a+b
    elif sign == "-":
        return a-b
    elif sign == "*":
        return a*b
    elif sign == "/":
        return a/b
    # else:
    #     return
    
def test():
    print("this is only a test")

test = "test"

def test():
    print("the new, much better test")

test()

print(sum([1,2,3,4,5]))

def sum(a, b):
    return a+b

print(sum(2, 3))

def test_arg(a, b, c, d):
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

test_arg(1,2,3,4)
test_arg(4,3,2,1)
# test_arg(4,3,2,1,0)
# test_arg(4,3)

def test_shared_links(a, b):
    a += 2
    b[0] += 2
    print(a, b)

target_int = 5
target_list = [5]
print(target_int, target_list)
test_shared_links(target_int, target_list)
print(target_int, target_list)

def no_results():
    print("I'm helpless")

def yes_result():
    return "yes", 1, 2, 3
    print("after the return")

x = yes_result()
y = no_results()
print(x, y)