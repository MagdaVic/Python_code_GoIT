from datetime import date


def get_days_in_month(month, year):
    number_days=27
    while True:
        try:
            number_days=number_days+1
            date(year,month,number_days)
        except ValueError:
            break
        else:
            max_days=number_days
    

    return max_days



month=2
year=2020
print(get_days_in_month(month, year))