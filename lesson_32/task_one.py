"""1. Write a function that calculates difference in days between two datetimes."""
# from datetime import datetime


# def get_difference_in_days(first_date: datetime, second_date: datetime) -> int:
#     difference = first_date - second_date
#     return difference.days


# first_date = datetime(2020, 2, 29, 18, 20, 50)
# second_date = datetime(2020, 2, 20, 18, 20, 50)

# print(get_difference_in_days(first_date, second_date))


"""2. Write a function that takes a datetime object, which will represent employees
   starting work day. and will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off"""

# from datetime import datetime, date


# def get_holidays(starting_date: date) -> int:
#     return int(
#         (
#             12 * (date.today().year - starting_date.year)
#             + date.today().month
#             - starting_date.month
#         )
#         * 1.6
#     )


# starting_date = date(2020, 2, 29)

# print(get_holidays(starting_date))

"""3. find next 3 Fridays that happend to be Friday the 13th (classic)"""

# import datetime

# today = datetime.datetime.today()

# i = 0
# while i < 3:
#     today = today + datetime.timedelta(days=1)
#     # print(today)
#     if today.strftime("%A %d") == "Friday 13":
#         print(today)
#         i += 1

"""4. Write a python function that takes nothing but returns the datetime object of last Friday"""

# import datetime


# def get_last_friday() -> str:
#     today = datetime.datetime.today()
#     while True:
#         today = today - datetime.timedelta(days=1)
#         if today.weekday() == 4:
#             return today.strftime("%Y-%m-%d")


# print(get_last_friday())

"""5. Write a Python program to get the last day of a specified year and month, Example: Monday, Tuesday etc."""

# import datetime


# def last_day_of_month(any_day):
#     next_month = any_day.replace(day=28) + datetime.timedelta(
#         days=4
#     )  # this will never fail
#     return next_month - datetime.timedelta(days=next_month.day)


# last_day_of_month(2023, 4)

from datetime import date,timedelta

def lastday_month(year,month):
    try:
    d=date(year,month,1)
    d1=d.replace(d.year,d.month+1,1)
    d = (d+ (d1-d)) - timedelta(1)
    return d.day
#if month is 12 then handled in exception
    except ValueError:
        print('x')
        d=date(year,month,1)
        d1=d.replace(d.year + 1,1,1)
        d = (d+ (d1-d)) - timedelta(1)
        return d.day

print(lastday_month(2017,12))
print(lastday_month(2017,11))
print(lastday_month(2017,2))