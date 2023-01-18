def make_request(keys, values):
    dict_res={}
    if len(keys)!=len(values):
        return dict_res
    for ind,key in enumerate(keys):
        dict_res[key]=values[ind]
    return dict_res
    
    

keys=[1,2,3,4]
values=['a','b','c','d']
print(make_request(keys, values))
