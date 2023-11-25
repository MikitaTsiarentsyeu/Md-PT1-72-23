slovo = str(input('Введите слово:'))
a = slovo[::-1]
if slovo == a:
  print("Палиндром")
else:
  print("Не палиндром")