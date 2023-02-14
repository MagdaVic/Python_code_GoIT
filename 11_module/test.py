from datetime import datetime

def days_to_birthday(birthday):
    birthday=datetime.strptime(birthday, '%d.%m.%Y')
    now = datetime.now()
    delta1 = datetime(now.year, birthday.month, birthday.day)
    delta2 = datetime(now.year+1, birthday.month, birthday.day)
    return ((delta1 if delta1 > now else delta2) - now).days



birthday='10.02.1976'

print(days_to_birthday(birthday))

x1,*x2=[]
print(x1)