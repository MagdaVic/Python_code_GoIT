def decode(data, lst_res=None):
    if lst_res is None:
        lst_res=[]
    if len(data)==0:
        return 0
    for ind in range(len(data)-1):
        lst_res.extend(data[ind]*data[ind+1])
        decode(data[ind+2:],lst_res)
        return lst_res
    




data=["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
print(decode(data))