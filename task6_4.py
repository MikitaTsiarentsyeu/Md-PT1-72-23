def exp(number, power):
    # perhaps, the power is null
    if power == 0:
        return 1
    # perhaps, the power is 1
    elif power == 1:
        return number
    # if the power  != 0 or 1
    elif power != 0 and power != 1:
        # [1:] - go to the right of the 1 (second) item
        return (number * exp(number, power-1))
number = int(input("Enter the number:"))
power = int(input("Enter the power:"))
print("Result = ", exp(number, power))
