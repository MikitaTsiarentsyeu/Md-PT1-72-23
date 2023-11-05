str = str.casefold("My name is Alex eee")
vowels = "aeiou"
result = [i for i in str if i in vowels]

print(len(result))