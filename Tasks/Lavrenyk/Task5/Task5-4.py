def low_upp(string: str) -> tuple:
    low_case, upp_case = 0, 0

    for i in string:
        if i.islower():
            low_case += 1
        elif i.isupper():
            upp_case += 1

    return low_case, upp_case

