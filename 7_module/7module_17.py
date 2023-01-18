
# def encode(data):  
#     if len(data) == 0:  
#         return []  

#     index = 1  
#     while index < len(data) and data[index] == data[index - 1]:  
#         index = index + 1  

#     current = [data[0], index]  

#     return current + encode(data[index : len(data)]) 
    
def encode(data, lst_res=None):
    if lst_res is None:
        lst_res=[]
    if len(data)==0:
        return []
    counter=1
    for ind in range(1,len(data)):
        if data[ind]==data[ind-1]:
            counter=counter+1
            continue
        else:
            break
    lst_res.extend([data[ind],counter])
           
    encode(data[counter:len(data)], lst_res)
    return lst_res

data=["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]
print(encode(data))