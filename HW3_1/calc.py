
num1 = float(input("Введіть перше число: "))
action = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

if action == "+":
    result = num1 + num2
    print("Результат:", result)

elif action == "-":
    result = num1 - num2
    print("Результат:", result)

elif action == "*":
    result = num1 * num2
    print("Результат:", result)

elif action == "/":
    if num2 != 0:
        result = num1 / num2
        print("Результат:", result)
    else:
        print("Помилка! На нуль ділити не можна!")

else:
    print("Помилка! Невідома математична дія.")
