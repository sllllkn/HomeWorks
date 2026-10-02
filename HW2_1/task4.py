price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Ціна зі знижкою:", final_price)