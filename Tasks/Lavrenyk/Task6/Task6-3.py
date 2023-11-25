def countC(in_str, char, i=0, count=0):
    if i == len(in_str):
        return count
    else:
        if in_str[i] == char:
            return countC(in_str, char, i + 1, count + 1)
        else:
            return countC(in_str, char, i + 1, count)
