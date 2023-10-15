import decimal

a = decimal.Decimal(input("Enter the amount (in dollars and cents): "))
b = decimal.Decimal('3.2954')
c = (a*b)
print("Your amount in BYN: ", round(c,2))