True
False

print(3 > 1)
print(3 <= 1)

print(type(False), type(True))

print(1 == True)
print(0 == False)

print(isinstance(True, int))
print(isinstance(False, int))

print(True+True+False)

print(False and False)

x = 55

print(x > 0 and x < 10)

print(True or False)

print(x > 0 or x < 10)

print(not True)
print(not False)

print(1, bool(1))
print(0, bool(0))
print(100, bool(100))
print(-5, bool(-5))
print(0.00000000000000001, bool(0.00000000000000001))

print("", bool(""))
print(" ", bool(" "))
print([], bool([]))
print([1,2,3], bool([1,2,3]))

text1 = "some text"
text2 = ""

print(text1 and text2)
print(text1 or text2)

res = print("some printed text")
print(res, bool(res))

print("left") and print("right")