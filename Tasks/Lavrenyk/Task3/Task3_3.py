user_input = input('Input a string: ').split()
set_user_input = set(user_input)

counts = {i: user_input.count(i) for i in set_user_input}
for k, v in counts.items():
    print(f'"{k}": {v}')