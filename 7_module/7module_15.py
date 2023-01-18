# lst_res=[]
# def flatten(data):
#     if not data:
#         return []
#     for i, el in enumerate(data):
#         if type(data[i]) is list:
#            flatten(data[i]) 
#         else:
#             lst_res.append(el)
#     return lst_res

# def flatten(data):
#     flat = []
#     def helper(data):
#         for e in data:
#             if isinstance(e, list):
#                 helper(e)
#             else:
#                 flat.append(e)
#     helper(data)
#     return flat

def flatten(data, list_res=None):
    if list_res is None:
        list_res = []
    if isinstance(data, list):
        for i in data:
            flatten(i, list_res)
    else:
        list_res.append(data)
    return list_res


data= [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]] 
print(flatten(data))