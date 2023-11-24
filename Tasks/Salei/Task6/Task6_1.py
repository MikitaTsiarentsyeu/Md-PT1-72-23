str_base = "Write a recursive function to reverse a string."

def rev_str(s):
    if len(s) == 0:
        return s
    else:
        return rev_str(s[1:]) + s[0]

print(rev_str(str_base))