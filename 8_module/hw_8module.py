from datetime import date, datetime, timedelta
import sys

def get_dict_week_names(users):
    current_date = datetime.now().date()
    for i in users:
        difference_days=(i['birthday'].date()-current_date).days
        if (current_date.weekday()==0 and -2<=difference_days<=4) or (current_date.weekday()>0 and 0<=difference_days<=6):
            for k,v in dict_week_days.items():
                if i['birthday'].weekday() in v:
                    dict_week_names[k].append(i['name'])
       
    return dict_week_names

def validate_correct_path():
    try:
        sys.argv[1]=='print'
    except IndexError:
        sys.exit("Write word 'print'")
    if sys.argv[1]!='print':
        sys.exit("Write word 'print'")


def print_out_in_console(dict_week_names):
    for k,v in dict_week_names.items():
            print(f"{k}: {', '.join(v)}")

def get_birthdays_per_week():
    validate_correct_path()
    dict_week_names=get_dict_week_names(users)
    print_out_in_console(dict_week_names)



if __name__ == '__main__':
    users=[{'name':'1','birthday':datetime(year=2023, month=1, day=21, hour=14)},{'name':'Olya','birthday':datetime(year=2023, month=1, day=20, hour=14)},{'name':'Den','birthday':datetime(year=2023, month=1, day=23, hour=14)},{'name':'4','birthday':datetime(year=2023, month=1, day=24, hour=14)},{'name':'5','birthday':datetime(year=2023, month=1, day=24, hour=14)},{'name':'6','birthday':datetime(year=2023, month=1, day=27, hour=14)},{'name':'Alla','birthday':datetime(year=2023, month=1, day=28, hour=14)}, {'name':'8','birthday':datetime(year=2023, month=1, day=30, hour=14)}]
    dict_week_days={'Monday':[0,5,6], 'Tuesday':[1], 'Wednesday':[2], 'Thursday':[3],'Friday':[4]}
    dict_week_names={'Monday':[], 'Tuesday':[], 'Wednesday':[], 'Thursday':[],'Friday':[]}
    get_birthdays_per_week()



