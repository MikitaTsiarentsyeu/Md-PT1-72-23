import random

from_num = int(input('From number: '))
to_num = int(input('To number: '))
random_num = random.randint(from_num, to_num)
print(f'Your number is {random_num}')
