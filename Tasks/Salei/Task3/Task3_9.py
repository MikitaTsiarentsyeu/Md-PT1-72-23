user_input = "Write a program that takes a string as input and returns the string reversed"
l = list(user_input)
reverse_l = []

for i in range(len(l)-1, -1, -1):
    reverse_l.append(l[i])

print("".join(reverse_l))