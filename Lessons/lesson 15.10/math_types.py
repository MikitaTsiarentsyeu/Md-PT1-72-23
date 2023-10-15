import decimal
import math
import random

x = 5+98*(-45)
print(x, type(x))

1, 0

print(type(12/4), type(12//4))

print(round(3.55555, 2))
print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))

print(type(int(10.1)))

x = 1.1
print(type(x))

print(1.1+1.1+1.1==3.3)
print(1.1+1.1+1.1)

print(5+8.0)
print(float(2))

x = decimal.Decimal(1.1)
print(x+x+x)

x = decimal.Decimal('1.1')
print(x+x+x)

math.pow(2, 3)
math.sqrt(144)

2**3
144**0.5

print(math.pi, math.e)

print(type(math.inf))

print(1000000000000000>math.inf)
print(math.inf*154654654645)
print(math.inf>math.inf)

print(10/math.inf)
print(math.inf/math.inf)

print(math.nan+5)
print(math.nan == math.nan)

print(random.randint(1, 10))