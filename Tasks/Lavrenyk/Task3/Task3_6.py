lower_case_vowels = 'ауоыиэяюёе'
vowels = f'{lower_case_vowels}{lower_case_vowels.upper()}'

user_input = input('Input any string: ')

for i in vowels:
    if i in user_input:
        user_input = user_input.replace(i, '')

print(user_input)