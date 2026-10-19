def find_unique_value(some_list):
    for number in some_list:
        count = 0
        for other in some_list:
            if number == other:
                count += 1
        if count == 1:
            return number


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("OK")