vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
user_input = "Write a program that takes a string as input from a user \
            and returns the number of vowels in the string."
count = 0
for i in user_input:
    if i in vowels_list:
        count+=1
print(f"Count vowels in user input is {count}")
