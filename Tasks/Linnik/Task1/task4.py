import decimal

print('from USD to BYN')
usd_money = decimal.Decimal(input("Please, fill in your number of US money.\n"))
byn_money = usd_money * decimal.Decimal('3.35')
print(byn_money, 'BYN')
