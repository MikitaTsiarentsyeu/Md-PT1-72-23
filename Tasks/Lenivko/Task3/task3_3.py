# A program that takes a string as input and returns a dictionary with the count of each word in the string.

text = input().split()
dict = {}
for i in range(len(text)):
    dict[i+1] = text[i]
print(dict)