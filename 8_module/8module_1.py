from datetime import datetime


def get_days_from_today(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.now()
    days_difference = current_date-date

    return days_difference.days