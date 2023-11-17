
user_string = 'People start learning a foreign Language, because they want to have a Better Job'
def count_letters(user_string):
    return sum(i.isupper() for i in user_string), sum(j.islower() for j in user_string)
print(count_letters(user_string))