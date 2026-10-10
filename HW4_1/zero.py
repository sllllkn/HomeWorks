
def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zeros + zeros


print(move_zeros([0, 1, 0, 12, 3]))
print(move_zeros([0]))
print(move_zeros([1, 0, 13, 0, 0, 5]))
print(move_zeros([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
