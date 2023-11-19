# 1. Write a recursive function to reverse a string.
def reverse_str(string, counter=1, res=[]):
    if (1 or 0) == len(string):
        return string
    if counter != len(string):
        counter += 1
        reverse_str(string, counter)
    res.append(-counter)
    return counter - 1






# 2. Write a recursive function to check whether a given string is a palindrome.
def palindrome(string):
    pass


# 3. Write a recursive function to count the number of occurrences of a given character in a string.
def num_letter(symbol, string):
    pass


# 4. Write a recursive function to calculate the power of a given number.
def pow_num(num, power):
    pass


# 5. Write a recursive function to find the Nth number in the Fibonacci sequence.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21
#
# n = 6 => 5
def fibonacci(nth):
    pass
