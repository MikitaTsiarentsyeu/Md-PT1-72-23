my_list=[65,34,6,1,7,51,73,34,64]
prime_numbers = []
for i in my_list:
    if i%2 != 0 and i%3!=0 and i%5 !=0:
        prime_numbers.append(i)
print(prime_numbers.sort[-1] )