import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2003, month=7, day=18, hour=8)
print(date_of_birth)
