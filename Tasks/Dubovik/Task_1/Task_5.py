import random

left_border = int(input("Please input left border number for random: "))
right_border = int(input("Please input right border number for random: "))
random_number = random.randint(left_border, right_border)
print("Your random number is: ",random_number)
