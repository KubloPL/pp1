eur_buy_rate = float(input("Enter bank buy EUR rate: "))
eur_sell_rate = float(input("Enter bank sell EUR rate: "))

spread = eur_sell_rate - eur_buy_rate

print("Spread: ", round(spread, 4))
