s = input()
s = s.split(' ')
d = {}
counter = 0
for word in s:
    counter += 1
    d[word] = d.get(word, 0) + counter
print (d)