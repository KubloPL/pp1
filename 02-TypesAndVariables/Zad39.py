price = float(input("Enter price: "))
discount_percent = float(input("Enter discount %: "))
discount = discount_percent / 100

price_with_discount = price - (price * discount)
reduction = price - price_with_discount

print(f"Price with discount: {
      round(price_with_discount, 2)} \n Reduction: {round(reduction, 2)}")
