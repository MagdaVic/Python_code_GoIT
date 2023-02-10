import re


def generator_numbers(string=""):
    if string == "":
        return []
    list_num = re.findall(r'\d+', string)
    i = 0
    while i <= len(list_num)-1:
        yield list_num[i]
        i = i+1


def sum_profit(string):
    gener_index_res = generator_numbers(string)
    sum_number = 0
    for i in gener_index_res:
        sum_number = sum_number+int(i)
    return sum_number


string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."


print(sum_profit(string))
