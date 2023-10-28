# Write a program that calculates the area of a circle given its radius, ask a user for the radius.
from math import pi

r = float(input("Enter the radius of the circle: "))
S = pi*r**2
print("The area of ​the circle is", round(S, 2))