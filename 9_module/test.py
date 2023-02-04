x1, x2, *x3 = [1, 2, 3, 4]
print(x1, x2, *x3)

random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)


# converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)
