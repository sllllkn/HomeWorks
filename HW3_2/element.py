
def last_to_first(numbers):
    if len(numbers) > 1:
        numbers.insert(0, numbers.pop())
    return numbers


print(last_to_first([12, 3, 4, 10]))
print(last_to_first([1]))
print(last_to_first([]))
print(last_to_first([12, 3, 4, 10, 8]))
