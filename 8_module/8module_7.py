import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    lst_res=[]
    if isinstance(cats[0],tuple):
        for cat in cats:
            lst_res.append({"nickname": cat.nickname, "age": cat.age, "owner": cat.owner})
    if isinstance(cats[0],dict):
        for cat in cats:
             lst_res.append((cat["nickname"],cat["age"],cat["owner"]))
    
    return lst_res
        
        # return[{"nickname":Cat.nickname , "age": Cat.age, "owner": Cat.owner} for i in cats]




cats= [{"nickname": "Mick", "age": 5, "owner": "Sara"},
{"nickname": "Barsik", "age": 7, "owner": "Olga"},
{"nickname": "Simon", "age": 3, "owner": "Yura"},
]
print(convert_list(cats))

#     [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"},
# ]
# [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]