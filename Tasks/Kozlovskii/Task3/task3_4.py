a = input('Enter:')
b = a.split(' ')
c = [int(i) for i in b]
result = 0

for j in range(len(c)-1):
    max_i = j
    for i in range(j+1, len(c)):
        if c[i]<c[max_i]:
            max_i = i
    c[max_i], c[j] = c[j], c[max_i]
print(c[1])