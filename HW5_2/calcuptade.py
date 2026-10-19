
while True:
    num1 = float(input("Введіть перше число: "))
    action = input("Введіть дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if action == "+":
        print("Результат:", num1 + num2)

    elif action == "-":
        print("Результат:", num1 - num2)

    elif action == "*":
        print("Результат:", num1 * num2)

    elif action == "/":
        if num2 != 0:
            print("Результат:", num1 / num2)
        else:
            print("Помилка! На нуль ділити не можна!")

    else:
        print("Помилка! Невідома математична дія.")

    answer = input("Бажаєте продовжити? (yes/no): ").lower()

    if answer not in ("yes", "y"):
        print("Роботу калькулятора завершено.")
        break
