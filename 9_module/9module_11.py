from functools import reduce


def sum_numbers(numbers):
    result_sum = reduce(lambda i, j: i+j, numbers, 0)
    return result_sum


numbers = [3, 4, 6, 9, 34, 12]
print(sum_numbers(numbers))
