try:
    # enter the  value in degrees Celsius
    a = float(input("enter the temperature in degrees Celsius"))
    # determine the temperature in degrees Fahrenheit (formule)
    b = float((5 / 9) * a + 32)
    print("temperature in degrees Farengeyt", "=", round(b, 1))
except (ValueError):
    print("You can only enter a numeric value")
