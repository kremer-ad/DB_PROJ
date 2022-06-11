from random import randrange,choice
from datetime import datetime,timedelta
from sys import argv

CURRENT_YEAR = '2022'

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def generate_two_dates(start_year):
    start = datetime.strptime(f'1/1/{start_year} 1:00 AM','%m/%d/%Y %I:%M %p')
    end = datetime.strptime(f'1/1/{CURRENT_YEAR} 1:00 AM','%m/%d/%Y %I:%M %p')
    ret_start = random_date(start,end)
    latest_end = ret_start + timedelta(days=14)
    ret_end =  random_date(ret_start,latest_end)
    return ret_start,ret_end

a,b = generate_two_dates('2017')
#'%d %m %Y %H:%M'
print(a.strftime('%Y/%m/%d %H:%M:%S'))