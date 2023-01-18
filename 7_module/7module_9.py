# def all_sub_lists(data):
#     lst_sub=[]
#     lst_res=[[]]
#     for i in data:
#         lst_sub.append(i)
#         lst_res.append(lst_sub)
#         lst_sub=[]
#         for j in data[i+1:]:
#             lst_sub.extend(data[i:j])
#             lst_res.append(lst_sub)
#             lst_sub=[]

#     return lst_res

def all_sub_lists(data):
    lst_res=[[]]
    for i in range(len(data)+1):
        for j in range(i+1,len(data)+1):
            lst_sub=[]
            lst_sub.extend(data[i:j])
            lst_res.append(lst_sub)
    lst_res.sort(key=len)
                    
    return lst_res       


data=[1, 2, 3] #[[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]

print(all_sub_lists(data))