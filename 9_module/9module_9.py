def positive_values(list_payment):
    list_positive_payment = list(filter(lambda i: i >= 0, list_payment))
    return list_positive_payment


list_payment = [100, -3, 400, 35, -100]
print(positive_values(list_payment))
