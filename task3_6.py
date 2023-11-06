# String for input
# People start learning a foreign language, because they want to have a better job.
capitals = 'AEIOUY'
All = f'{capitals}{capitals.lower()}'
#print (All)
user_input = input('Input anything: ')
for i in All:
    if i in user_input:
        user_input = user_input.replace (i, " ")
# Первый параметр — строка, которую нужно заменить, второй — строка, которой нужно заменить вхождения
print (user_input)
