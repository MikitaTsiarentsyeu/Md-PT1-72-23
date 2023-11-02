# A program takes a list of numbers as input and returns the largest prime number in the list.

from random import randint


li = []
for _ in range(10):
    li.append(randint(2, 20))
print(li)
largest_prime = 0

for i in range(len(li)):
    counter = 0
    for j in range(1, li[i]+1):
        if li[i] % j == 0:
            counter += 1
    if counter == 2 and counter > largest_prime:
        largest_prime = li[i]
print(largest_prime)