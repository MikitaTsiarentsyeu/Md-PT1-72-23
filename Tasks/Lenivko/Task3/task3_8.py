# A program takes a list of numbers as input and returns the average of all numbers in the list.
from random import randint

# to simplify task verification, the random module was used instead of entering numbers.
li = []
for _ in range(10):
    li.append(randint(1, 100))
print(li)
total = 0
for i in li:
    total += i
print(total / len(li))