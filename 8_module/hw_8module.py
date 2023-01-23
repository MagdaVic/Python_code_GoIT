from datetime import date, datetime, timedelta
import sys

def get_birthdays_per_week(users):
    dict_week_days={'Monday':[0,5,6], 'Tuesday':[1], 'Wednesday':[2], 'Thursday':[3],'Friday':[4]}
    dict_week_names={'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[],'Friday':[]}
    # if sys.argv[1]=='print':
    current_date = datetime.now().date()
    # list_difference_days =[timedelta(days=i) for i in range(7)]
    list_res_days=[]
    for i in users:
        difference_days=int((i['birthday'].date()-current_date).days)
        if (current_date.weekday()==0 and -2<=difference_days<=4): #or (current_date.weekday>0 and 0<=difference_days<=6):
            for k,v in dict_week_days.items():
                if i['birthday'].weekday() in v:
                    dict_week_names[k].append(i['name'])
        
        
    return dict_week_names

   


users=[{'name':'Bob','birthday':datetime(year=2023, month=1, day=21, hour=14)},{'name':'Aob','birthday':datetime(year=2023, month=1, day=20, hour=14)},{'name':'Oob','birthday':datetime(year=2023, month=1, day=23, hour=14)},{'name':'EEb','birthday':datetime(year=2023, month=1, day=24, hour=14)},{'name':'GGob','birthday':datetime(year=2023, month=1, day=24, hour=14)},{'name':'FDFb','birthday':datetime(year=2023, month=1, day=27, hour=14)},{'name':'Bab','birthday':datetime(year=2023, month=1, day=28, hour=14)}, {'name':'Bnb','birthday':datetime(year=2023, month=1, day=30, hour=14)}]

print(get_birthdays_per_week(users))
# get_birthdays_per_week(users)