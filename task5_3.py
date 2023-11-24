fruits = ['apple', 'banana', 'mango', 'watermelon', 'plum']
big_friuts = []
def long_str(a):
    for i in a:
        if len(i) > 5:
            big_friuts.append(i)
    return big_friuts
print(long_str(fruits))