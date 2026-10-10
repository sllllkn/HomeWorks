
def checkio(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers[i] for i in range(0, len(numbers), 2))
    return total * numbers[-1]


print(checkio([0, 1, 7, 2, 4, 8]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))
