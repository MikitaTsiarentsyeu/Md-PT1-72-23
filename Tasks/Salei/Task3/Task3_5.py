# Write a program that takes a list of strings as input and returns a 
# list with all strings that have a length greater than 5 characters.
user_input = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]
l = []
for i in user_input:
    if len(i) > 5:
        l.append(i)
print(l)