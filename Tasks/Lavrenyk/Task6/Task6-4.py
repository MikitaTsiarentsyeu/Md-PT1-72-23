def power(n, n_pow, res=1):
    if n_pow == 0:
        return res
    else:
        return power(n, n_pow - 1, res*n)
