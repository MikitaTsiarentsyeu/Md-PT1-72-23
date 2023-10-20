# import the module Decimal:
from decimal import Decimal
try:
    # enter a fixed dollar exchange rate:
    u = Decimal("3.299")
    u = u.quantize(Decimal("1.0000"))
    # enter a sum in dollars:
    n = Decimal(input("Enter a sum in dollars"))
    b = n * u
    print("Sum in BYN:", round(b, 4))
except (ValueError, Decimal.InvalidOperation, NameError, AttributeError):
    print("You can only enter a numeric value")
