# from datetime import datetime

# def days_to_birthday(birthday):
#     birthday=datetime.strptime(birthday, '%d.%m.%Y')
#     now = datetime.now()
#     delta1 = datetime(now.year, birthday.month, birthday.day)
#     delta2 = datetime(now.year+1, birthday.month, birthday.day)
#     return ((delta1 if delta1 > now else delta2) - now).days


# birthday='10.02.1976'

# print(days_to_birthday(birthday))

# x1,*x2=[]
# print(x1)

def iterator(data_dict, n=3):
    index = 0
    lst_temp = []
    for k, v in data_dict.items():
        if index < n:
            lst_temp.append(v)
            index = index+1
        else:
            yield lst_temp
            lst_temp = []
            index = 1
            lst_temp.append(v)
    yield lst_temp


def show_all_limit(data_dict, n=3):
    step = iterator(data_dict)
    for i in data_dict:
        try:
            print(next(step))
        except StopIteration:
            break


data_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'x': 4}
show_all_limit(data_dict)
print(iterator(data_dict))
