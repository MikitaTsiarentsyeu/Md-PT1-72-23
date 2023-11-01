# 10. Write a program that takes a list of numbers as input
# returns the largest prime number in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Prime numbers: 2, 3, 5, 7, 11, 13. One isn't included.
largest_prime_num = ''
for i in numbers:
    flag = True
    if i <= 1:
        continue
    for j in range(2, 8):
        if i % j == 0:
            flag = False
    if flag:
        if largest_prime_num == '' or largest_prime_num < i:
            largest_prime_num = i
print(largest_prime_num)
