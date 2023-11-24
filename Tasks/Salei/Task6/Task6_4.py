c = 2

def my_pow(a, b, c, res = None):
    if b == 0:
        return 1
    if b == 1:
        return a
    if c > b:
        return res
    if c == 2:
        res = a*a
        return my_pow(a, b , c + 1, res)
    if c > 0:
        res = res * a
        return my_pow(a, b, c + 1, res)

print(my_pow(3, 3, c))


 
