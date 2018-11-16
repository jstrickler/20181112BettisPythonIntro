#!/usr/bin/env python
from datetime import date, datetime, timedelta
import time

now = datetime.now()
print(now)
print(dir(now), '\n')
print(now.day, now.hour)
print(time.time())

today = date.today()
james_bd = date(2014, 8, 1)
elapsed = today - james_bd
print(dir(elapsed))
years = elapsed.days / 365.25
days = elapsed.days % 365
# years, days = divmod(elapsed.days, 365)
print("James is {:.2f} years and {} days old".format(years, days))


