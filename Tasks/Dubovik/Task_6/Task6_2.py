str = "Alex"
str2 = "mom"

def palindrome(str):
    if len(str) < 1:
        return True
    else:
        if str[0] == str[-1]:
            return palindrome(str[1:-1])
        else:
            return False


if palindrome(str2) == True:
    print("Palindrome")
else:
    print("NOT Palindrome")


print(palindrome(str))
print(palindrome(str2))


