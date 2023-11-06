list = ["abcde", 'mynameis', "animal", "oxygen"]
list2 = []
for i in list:
    if len(i) > 5:
        list2.append(i)

print(list2)