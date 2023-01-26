from datetime import datetime
 
def get_str_date(date):

    date_res = datetime.strptime(date.split()[0], '%Y-%m-%d').strftime('%A %d %B %Y')

    return date_res 
   



date='2021-05-27 17:08:34.149Z' #'Thursday 27 May 2021'
print(get_str_date(date))