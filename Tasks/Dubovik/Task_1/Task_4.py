import decimal

currency_exchange_rate = decimal.Decimal(3.293)
byn = decimal.Decimal(input("Please, input USD amount: "))
usd = currency_exchange_rate*byn
print("Exchange rate is", round(usd, 2), "BYN")
