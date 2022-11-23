from datetime import datetime
from random import random


def randomDate(start_date, end_date):
    #start_date = datetime.date(2020, 1, 1)
    #end_date = datetime.date(2020, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def randomData():
    resL = []
    for i in range(0,20):
        resL.append([
            randomDate(datetime.date(2022, 1, 1), datetime.date(2022, 2, 1)),
            random.randint(1, 100),
            random.randint(0, 1)
        ])
    return resL

