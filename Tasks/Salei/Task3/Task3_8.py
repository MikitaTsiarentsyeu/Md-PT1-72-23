# Write a program that takes a list of numbers as input and returns 
# the average of all numbers in the list.

user_input = [16, 146, 11, 108, 399, 512, 1005, 22, 1137]
sum = 0
for i in user_input:
    sum += i
print(int(round(sum/len(user_input), 0)))