import datetime
import random

START_DATE = datetime.date(1922, 1, 1)
END_DATE = datetime.date(2004, 2, 1)


def random_date():
    time_between_dates = END_DATE - START_DATE
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = START_DATE + datetime.timedelta(days=random_number_of_days)
    return random_date
