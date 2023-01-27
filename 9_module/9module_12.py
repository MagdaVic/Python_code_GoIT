from functools import reduce


def amount_payment(payment):
    result_sum = reduce(lambda i, j: i+j, filter(lambda i: i > 0, payment), 0)
    return result_sum


payment = [1, -3, 4]
print(amount_payment(payment))
