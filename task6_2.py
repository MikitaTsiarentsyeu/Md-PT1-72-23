def palindrome(string):
    # perhaps, the line is null
    if len(string) == 0:
        return True
    else:
        # if the 1 item = the last item
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False
user_string = str(input("Enter the string:"))
if (palindrome(user_string) == True):
    print("Your string is palindrome")
else:
    print("Your string isn't palindrome")