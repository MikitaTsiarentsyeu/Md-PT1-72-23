Enter = input('')
gls = 0
for i in Enter:
    if i in "аеёиоуыэюяАЕЁИОУЫЭЮЯ":
        gls += 1
print("Количество гласных: ", gls)


