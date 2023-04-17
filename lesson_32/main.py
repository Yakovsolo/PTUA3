import datetime

# x = datetime.datetime.today()
# print(type(x))

# x = datetime.date.today()
# print(type(x))

# x = datetime.datetime.today().time()
# print(x)

# y = datetime.datetime.today()
# print(y)

# print(y.strftime("%Z"))

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, "lt_LT.UTF-8")
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime

# now = datetime.datetime.now()

# now2 = datetime.datetime.now()
# print(type(now2 - now))
print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))

# 2020-11-25 12:26:14.575023
# 2020-11-20 12:26:14.575023
# 2020-11-25 17:26:14.575023
# 2020-12-15 20:26:14.575023

import datetime

pradzia = datetime.datetime.today()
for x in range(10000):
    print(x)

pabaiga = datetime.datetime.today()
print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")
