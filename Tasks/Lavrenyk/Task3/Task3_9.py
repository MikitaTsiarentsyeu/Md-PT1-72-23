def reverse_without_slice(s: list) -> str:
    i_range = range(len(s))
    j_range = range(len(s) - 1, -1, -1)

    half_range = [(i_range[k], j_range[k]) for k in range(len(s))][:len(s) // 2]

    for i, j in half_range:
        buff = s[i]
        s[i] = s[j]
        s[j] = buff

    return ''.join(s)


user_input = input('Input a string: ')
print(reverse_without_slice(list(user_input)))