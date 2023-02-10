def normal_name(list_name):
    list_name_res = list(map(lambda i: i.capitalize(), list_name))
    return list_name_res


# def normal_name(list_name):
#     list_name_res = list(map(str.capitalize, list_name))
#     return list_name_res

list_name = ["dan", "jane", "steve", "mike"]
print(normal_name(list_name))
