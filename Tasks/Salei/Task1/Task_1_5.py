# Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for the left and right border.
import random

lb_input = int(input("Enter the left boarder of the range as an integer: "))
rb_input = int(input("Enter the right boarder of the range as an integer: "))
print("A random number in the range", lb_input, "-", rb_input, "is", random.randint(lb_input, rb_input))