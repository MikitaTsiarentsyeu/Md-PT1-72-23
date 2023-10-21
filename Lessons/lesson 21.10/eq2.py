a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
c = int(input("Enter the c value: "))

D = b*b - 4*a*c

if D < 0:
    print("no roots can be calculated")
elif D == 0:
    x = -b/(2*a)
    print(x)
else:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(x1, x2)
