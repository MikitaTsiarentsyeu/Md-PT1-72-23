def get_ranges(our_string):
    res = []
    j = 0
    k = 0
    for i in range(1, len(our_string)):
        if our_string[i] == k + 1:
            k = our_string[i]
        else:
            if j == k:
                res.append(str(j))
            else:
                res.append(f"{j}-{k}")
            j = k = our_string[i]
    if j == k:
        res.append(str(j))
    else:
        res.append(f"{j}-{k}")
    return ", ".join(res)
our_string = [0, 1, 2, 3, 4, 7, 8, 10]
print(get_ranges(our_string))