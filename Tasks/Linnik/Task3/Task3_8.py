# 8. Write a program that takes a list of numbers as input
# returns the average of all numbers in the list.
numbers = [1, 2, 3, 45, 56, 76, 100]
average = 0
for i in numbers:
    average += i
print(average/len(numbers))
