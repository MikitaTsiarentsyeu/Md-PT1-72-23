a = "a"
print(ord(a))
print(chr(65))
print(chr(650))
print(chr(6500))
print(chr(65000))
print(chr(650000))

s = " "
print(type(s), s, repr(s))

print(str(print))
print(print)

str1 = "test str"

str2 = 'test str'

str3 = '''test str'''

str4 = """test str"""

print(str1 == str2 == str3 == str4)

text = "I'm a human"
text = 'I\'m a human'

some_quote = '"London is the capital ...."'

test_str = '''
line 1
line 2
line 3
'''

print(test_str)
print(repr(test_str))

s = "my very long string"

print(len(s))
print(len(' '))
print(len(''))

print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[-1], s[-2], s[-3], s[-4], s[-5])

# s[0] = "n" error

print(s[0:7])
print(s[0:1])
print(s)
print(s[3:-3])
print(s[3:-3:2])

part = s[3:-3]
print(s, part)

reverse = s[::-1]
print(reverse)

print("test" in s)
print("my" in s)
print(" " in s)

print(s.find("my"))
print(s.find(" "))
print("           ".find(" "))
print("           ".count(" "))

s = "test" + " " + "str"
print(s)

s = "+"*10
print(s)

s = "TeSt StRiNg"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s)

s = "645654:ghfg-45"
s = s.replace('6', ' ').replace('-', ' ')
print(s)

print(s.split())
print(s.split(":"))

c, d, p = "cat", "dog", "parrot"
s = "a " + c + ", a " + d + " and a " + p
print(s)
"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot"

print("a {}, a {} and a {}".format(c, d, p))

print(f"a {c}, a {d} and a {p}")

x = 10

print(f"the answer is {'positive' if x > 0 else 'negative'}")

'positive' if x > 0 else 'negative'

if x > 0:
    'positive'
else:
    'negative'