# Write a program that takes a list of numbers as input and returns
#  the second largest number in the list

l = [24, 3, 158, 232, 17, 34, 29, 48, 152]
l.remove(max(l))
print(max(l))