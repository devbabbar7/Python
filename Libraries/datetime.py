from datetime import date, datetime
import time

date_time = datetime.fromtimestamp(time.time()) # datetime from epochs
print(date_time)
print(date_time.isoformat()) # converts any date, datetime, time into str

d = date(1996, 12, 11)
print(d)

dt = datetime.today()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.weekday()) # 6 (returns val 0 to 6)