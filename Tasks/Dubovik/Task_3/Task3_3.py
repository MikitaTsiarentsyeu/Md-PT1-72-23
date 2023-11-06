str = "My name is Alex alex alex"
str2 = str.split(" ")
count = dict()
for word in str2:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
print(count)