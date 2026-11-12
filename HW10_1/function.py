def sequence_rule(number):
    return number ** 2


def sequence_generator(start, n, function):
    for i in range(start, start + n):
        yield function(i)


start = int(input("Введіть початкове число послідовності: "))
n = int(input("Введіть кількість членів послідовності: "))

generator = sequence_generator(start, n, sequence_rule)

print("Числова послідовність:")

for element in generator:
    print(element)
