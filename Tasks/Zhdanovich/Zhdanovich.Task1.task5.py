import random
try:
    # enter the left border:
    a=int(input("Enter the left border"))
    # enter the right border:
    b=int(input("Enter the left border"))
    print (random.randint(a,b))
except (ValueError, NameError, AttributeError):
    print("You can only enter a numeric value")