# Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

def reverse(list):
    res = []
    for i in list:    
        rev_word=i[::-1]    
        res.append(rev_word)
    reverse_list = res[::-1]
    return reverse_list
print(reverse(input("Enter string list: ").split()))