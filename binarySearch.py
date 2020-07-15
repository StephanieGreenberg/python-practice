"""Iterative Binary Search"""


def binary_search(input_array, value):
    min, max = 0, len(input_array) - 1
    while max >= min:
        mid = min + (max - min) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            max = mid - 1
        else:
            min = mid + 1
    return -1


"""Recursive Binary Search"""


def recursive_binary_search(input_array, value):
    return recursive_bs_helper(input_array, value, 0, len(input_array) - 1)


def recursive_bs_helper(input_array, value, min, max):
    if max < min:
        return -1
    else:
        mid = min + (max - min) // 2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            return recursive_bs_helper(input_array, value, min, mid - 1)
        else:
            return recursive_bs_helper(input_array, value, mid + 1, max)


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
test_val3 = 1

# Test Iterative Binary Search
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))

print()

# Test Recursive Binary Search
print(recursive_binary_search(test_list, test_val1))
print(recursive_binary_search(test_list, test_val2))
print(recursive_binary_search(test_list, test_val3))
