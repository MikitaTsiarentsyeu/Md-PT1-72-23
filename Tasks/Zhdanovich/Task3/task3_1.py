# String for input
# People start learning a foreign language, because they want to have a better job.
capitals = 'AEIOUY'
All = f'{capitals}{capitals.lower()}'
#print (All)
user_input = input('Input anything: ')
count = 0
for i in user_input:
    if i in All:
        count += 1
print (count)
print(sum([user_input.count(i) for i in All]))