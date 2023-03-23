# Write a function that returns dates of the 5 upcoming Friday 13ths, with Year, month and date

from datetime import date
import calendar

start_day = date.today()
bad_fridays_list = []
# for day in range(start_day)
#     if day == (year, month, 13) and day == 'friday':
#         bad_fridays_list.append(day)
print(start_day)
