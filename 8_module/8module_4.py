from random import randrange,sample


def get_numbers_ticket(min, max, quantity):
    if min>=1 and max<=1000 and min < quantity < max:
        lst_res=sample([i for i in range(min,max+1)],k=quantity)
        lst_res.sort()
        return lst_res
    else:
        return []

min, max, quantity=2,3,2
print(get_numbers_ticket(min, max, quantity))

