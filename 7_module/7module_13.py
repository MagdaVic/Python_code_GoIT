def get_employees_by_profession(path, profession):
    with open(path,'r') as ph:
        lst=ph.readlines()
    lst_res=[]
    for i in lst:
        if i.find(profession) !=-1:
            lst_res.append(i.split()[0])
    str_res=' '.join(lst_res)
    return str_res    


path=r'D:\GitHub\Tutorial\7_module\test.py'
profession='cook'
print(get_employees_by_profession(path, profession))

