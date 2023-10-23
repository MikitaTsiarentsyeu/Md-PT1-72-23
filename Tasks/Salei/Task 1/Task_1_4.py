# Write a program that converts some amount of money from USD to BYN, ask a user for the amount, store the ratio inside the program itself.
from decimal import Decimal

e_r = Decimal('3.2954')    # 1 USD = 3.2954 BYN (16.10.2023)
x = int(input("Enter the amount you want to convert: "))
d = x*e_r
print("Your amount in BYN:", round(d, 2))