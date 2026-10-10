
def split_list(numbers):
    middle = (len(numbers) + 1) // 2
    return [numbers[:middle], numbers[middle:]]


print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))
