# Write a program that takes a string as input and returns a dictionary 
# with the count of each word in the string.
import collections

user_input = "Write a program that takes a string as input and returns a \
      dictionary with the count of each word in the string"

split_str = user_input.split()
c = collections.Counter()

for i in split_str:
    c[i] += 1
print(c)