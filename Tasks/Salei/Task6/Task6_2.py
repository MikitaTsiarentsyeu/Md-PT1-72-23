user_input = input("Please, enter your string:\n")
def pal(user_input, a = user_input[0], b = user_input[-1]):
    if a == b:
        return True
    if a != b:
        return False
    if a < b + 1:
        return pal(user_input, a + 1, b - 1)
    return True


if pal(user_input):
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")