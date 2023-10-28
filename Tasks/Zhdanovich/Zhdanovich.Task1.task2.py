import math
try:
    # enter the positive value of the circle's radius in meters
    r=float(input("enter the positive value of the radius in meters"))
    #determine the area of a circle (formule)
    A=float(math.pi*r**2)
    print("area of a circle", "=", round(A,2))
except (ValueError):
    print("You can only enter a numeric value")
