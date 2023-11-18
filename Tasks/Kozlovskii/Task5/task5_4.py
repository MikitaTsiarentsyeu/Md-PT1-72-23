a = input('Введите данные:')
def f(a):
  uppers = 0
  lowers = 0
  for char in a:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
    else:
      pass
  return(uppers, lowers)
print(f(a))