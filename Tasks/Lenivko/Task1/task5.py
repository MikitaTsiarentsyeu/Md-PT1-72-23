# This program is a random number generator.

from random import randint

num1 = int(input('Enter the starting point of the range: ' ))
print('Excellent!')
num2  = int(input('Now enter the end point of the range: ' ))
random_num = randint(num1, num2)
print('Good job, lad! Here is your random number:', random_num)