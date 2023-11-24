def suit_len(str_lst: list, length: int = 5) -> list:
    res = [one_str for one_str in str_lst if len(one_str) > length]
    return res

