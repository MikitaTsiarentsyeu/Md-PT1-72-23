import random

l = [3,2,5,4,6,7]

i = random.randint(0, len(l)-1)
j = random.randint(0, len(l)-1)

l[i], l[j] = l[j], l[i]
print(l)


def random_sort(l):
    counter = 0
    while not is_sorted(l):
        i = generate_index(l)
        j = i
        while i == j:
            j = generate_index(l)
        swap(l, i, j)
        counter += 1
        print(counter)

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False

    return True

def generate_index(l):
    return random.randint(0, len(l)-1)

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]


random_sort(l)
print(l)