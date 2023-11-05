lower_case_vowels = 'ауоыиэяюёе'
vowels = f'{lower_case_vowels}{lower_case_vowels.upper()}'

user_input = input('Input any string: ')

print(sum([user_input.count(i) for i in vowels]))

