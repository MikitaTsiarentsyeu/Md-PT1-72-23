while True:
    user_input = input("Input your value in format hh:mm\n")

    if len(user_input) != 5:
        print("the input is incorrect, it has invalid length, please try again")
        continue

    if user_input[2] != ':':
        print("the input is incorrect, it lacks ':' sign, please try again")
        continue

    if user_input.count(':') != 1:
        print("the input is incorrect, it should've exactly one ':' sign, please try again")
        continue

    hours, minutes = user_input.split(':')
    if not (hours.isdigit() and minutes.isdigit()):
        print("the input is incorrect, the hours and minutes values must be digits, please try again")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 23 or minutes > 59:
        print("the input is incorrect, the hours or minutes values are too high, please try again")
        continue

    break

print("the main logic goes here")