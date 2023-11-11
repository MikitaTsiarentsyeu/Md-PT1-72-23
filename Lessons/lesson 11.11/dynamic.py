def mult(a, b):
    res = a*b
    return res

print(mult(2, 3))
print(mult([1,2,3], 10))
print(mult("[1,2,3]", 10))
# print(mult("[1,2,3]", "10")) error

def mult(a, b):
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(a, float)):
        if b < 0:
            a, b = -a, -b 
        return low_level_mult(a, b, 0)
    elif (isinstance(a, list) and isinstance(b, int) and b > -1) or (isinstance(b, list) and isinstance(a, int) and a > -1):
        return low_level_mult(a if isinstance(b, int) else b, b if isinstance(b, int) else a, [])
    elif isinstance(a, str) and isinstance(b, int) and b > -1:
        return low_level_mult(a, b, "")

    return False

def low_level_mult(a, b, res):
    for i in range(b):
            res += a
    return res


print(mult(2, 3))
print(mult(-2, 3))
print(mult(2, -3))
print(mult(-2, -3))

print(mult([2], 3))
print(mult(2, [3]))
print(mult("2", 3))


def eq(a, b):
    for i in a:
        if i not in b:
            return False
    for i in b:
        if i not in a:
            return False
    
    return True

print(eq((1,2,3), [3,2,1]))
print(eq(("1","2","3"), "321"))


def sum_for_ints(a:int, b:int) -> int:
    """This function will add only int values"""
    if isinstance(a, int) and isinstance(b, int):
        return a+b



# def add(a, b):
#     return a+b

# def add(a, b, c):
#     return add(add(a, b), c)

# print(add(2,3,4))