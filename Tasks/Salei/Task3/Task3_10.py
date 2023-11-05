# Write a program that takes a list of numbers as input and returns
# the largest prime number in the list
user_input = [2, 4, 6, 3, 5, 7, 11, 31, 13, 16, 17, 37, 19, 23, 26, 29, 33, 51, 141, 149, 53]
prime_list = []
for i in user_input:
        d = 2
        while i % d != 0 and d*d <= i:
            d += 1
        if d*d > i:
            prime_list.append(i)
            # print(i)
print(max(prime_list))