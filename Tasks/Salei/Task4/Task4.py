while True:
    max_len = input("Enter a maximum number of characters per line, which must be greater than 35:")

    if not max_len.isdigit():
        print("The value entered must be a integer number, please try again")
        continue
    max_len = int(max_len)

    if max_len < 36:
        print("The number must be greater than 35, please try again")
        continue
    break

with open("text.txt", "r") as f:
    text = f.read().split()

new_line = ""
result = []
count = 0

for i in text:
    count += len(i)
    if count >= max_len:
        new_line += "\n"
        count = len(i)
    elif new_line != "":
        new_line += " "
        count +=1
    new_line += i

for j in new_line.split("\n"):
    num_space = max_len - len(j)
    while num_space > 0:
        j = j.replace(" ", "  ", num_space)
        num_space = max_len -  len(j)
    result.append(j+"\n")

with open ("res_text.txt", "w") as f:
    for i in result:
        f.write(i)
    
print(f"res_text.txt with {max_len} characters per line is ready")