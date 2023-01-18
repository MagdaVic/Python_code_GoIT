# import math
def data_preparation(list_data):

    new_list=[]
    for i in list_data:
        if len(i)>2:
            i.remove(min(i))
            i.remove(max(i))
        new_list.extend(i)
    # new_list.sort()
    new_list.reverse()

    return new_list

list_data=[[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
print(data_preparation(list_data))