n = 5

i = 0
while True:
    if i == n:
        break
    print("it's cycle")
    i += 1

def print_n_times(n, i=0):
    if i == n:
        return
    print("it's recusrion")
    print_n_times(n, i+1)

print_n_times(n)


l = [1,2,3, [4,5,6, [7,8,9, [0]]], 11]

# [1,2,3,4,5,6,7,8,9,0]

def flatten(l, res=None):
    res = [] if not res else res
    for i in l:
        if isinstance(i, list):
            flatten(i, res)
        else:
            res.append(i)

    return res

print(flatten(l))

num = 123

def digits_sum(num):
    if num == 0:
        return 0
    # digit = num % 10
    # sum = digits_sum(num // 10)
    return digits_sum(num // 10) + num % 10

print(digits_sum(num))