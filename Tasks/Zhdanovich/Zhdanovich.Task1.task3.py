try:
    # Enter a value of the speed in kilometers per hour
    v1=float(input("Enter a value of the speed in kilometers per hour"))
    #determine the speed in meters per second (formule)
    v2=float(v1*(1000/3600))
    print("The speed in meters per second"," =", round(v2,2))
except (ValueError):
    print("You can only enter a numeric value")