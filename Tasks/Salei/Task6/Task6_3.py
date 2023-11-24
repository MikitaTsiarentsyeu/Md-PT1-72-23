count = 0

def count_occurrences(user_input, given_char, count):
    if user_input == "":
        return count
    if user_input[0] == given_char:
        return count_occurrences(user_input[1:], given_char, count + 1)
    if user_input[0] != given_char:
        return count_occurrences(user_input[1:], given_char, count)
    

print(count_occurrences(input("Enter string:\n"), input("Enter char:\n"), count))
   