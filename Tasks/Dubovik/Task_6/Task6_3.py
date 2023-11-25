

s = 'My name is alex aaa'
s2 = "a"

def func(s, s2):
    n1 = len(s)
    n2 = len(s2)

    if (n1 == 0 or n1 < n2):
        return 0
    if (s[0: n2] == s2):
        return func(s[1:], s2) + 1

    return func(s[1:], s2)

print(func(s, s2))
