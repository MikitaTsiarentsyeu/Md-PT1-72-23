
a = list(map(int, input('Enter your numbers through spaces: ').split()))
lst = []
# the prime number is divisible without a remainder by 1 or itself
# find the dividers: j is i > divider > 1, i is required number (Eratocphene's method)
for i in a:
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            lst.append(i)
#print (lst)
print (max(lst))