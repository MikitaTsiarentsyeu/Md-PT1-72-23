my_list = [4, 2, 78, 1, 56, 98, 65, 34, 9, 111, 137, 203]
prime_lst = []
for i in my_list:
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        prime_lst.append(i)
prime_lst.sort()
print('Max prime number is',prime_lst[-1])
print(sorted(prime_lst)[-1])

max_prime = 0
for i in range(1, len(prime_lst)):
    if prime_lst[i] > prime_lst[max_prime]:
        max_prime = i
print(prime_lst[max_prime])
