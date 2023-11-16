def get_ranges(n_list: list) -> str:
    res = []
    i, j = 0, 0

    while i != len(n_list):
        res.append([str(n_list[i])])

        try:
            if n_list[i] + 1 == n_list[i + 1]:
                try:
                    while n_list[i] + 1 == n_list[i + 1]:
                        i += 1
                    res[j].append(str(n_list[i]))
                except Exception:
                    res[j].append(str(n_list[i]))
                    break
        except Exception:
            break

        i += 1
        j += 1

    final = ['-'.join(_) for _ in res]

    return ', '.join(final)
