import csv

with open("data.txt") as f:
    data = eval(f.read())

# print(type(data))
# print(data)
# print(eval('3+8'))
# eval('print("eval is evel")')

with open('test.csv', 'w') as f:
    for entry in data:
        f.write(f"{','.join([str(x) for x in entry])}\n")

new_data = []
with open('test.csv', 'r') as f:
    for entry in f:
        new_data.append(entry.strip('\n').split(','))

print(new_data)

headline = ['make', 'model', 'vol', 'pow', 'year', 'id']

new_data.insert(0, headline)

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_data)

with open('test.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line, type(line))

with open('test.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, headline)
    for line in reader:
        print(line, type(line))

input()