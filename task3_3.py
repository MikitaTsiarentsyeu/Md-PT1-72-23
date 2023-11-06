# String for input
# People start learning a foreign language, because they want to have a better job, a possibility to study abroad or take part in international conferences.
user_string = input('Input a text string: ').split()
set_user_string = set(user_string)

counts = {i: user_string.count(i) for i in set_user_string}
for a, b in counts.items():
    print(f'"{a}": {b}')