

# from itertools import islice
# a = [1, 2, 3, 4]
# print(a[2:6])
from itertools import islice
a = [1, 2, 3, 4]
print(a[2:6])

# def show_all(lst):
#     for i in islice(range(len(lst)), 0, len(lst), 2):
#         print(lst[i:i+2])


# lst = [45, 67, 78, 90, 54]
# print(show_all(lst))

# class A:
#     def __init__(self, lst, n):
#         self.lst = lst
#         self.n = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         tem_lst = []
#         if self.i > len(self.lst)-1:
#             raise StopIteration
#         else:
#             # tem_lst = self.lst[self.i:self.i+self.n]
#             # self.i = self.i+self.n
#             i_start = self.i
#             while self.i < i_start+self.n:
#                 tem_lst.append(self.lst[self.i])
#                 self.i = self.i+1
#                 if self.i > len(self.lst)-1:
#                     break

#             return tem_lst


# lst = [45, 67, 4, 8, 8]

# a = A(lst, 4)
# for i in a:
#     print(i)
from faker import Faker, Factory
import json

# fake = Faker()
fake=Factory.create('uk_UA')

users=[]
def create_fake(fake,users:list,filename,n=10):
    for i in range(n):
        user={}
        user['name']=fake.name()
        user['phone']=fake.phone_number()
        users.append(user)
        print(user)
    to_json(users,filename)

def to_json(users,filename):
    with open(filename,'w',encoding='utf-8') as fh:
        json.dump(users,fh,indent=4,ensure_ascii=False)
        print('Users were saved')


if __name__=='__main__':
    filename = r'12_module\users.json'
    create_fake(fake,users,filename,n=120)
    
    

