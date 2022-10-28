from datetime import date, datetime, time

print(datetime.now())
print(datetime(2020, 10, 10))
print(datetime(2020, 10, 10, 10, 11, 12))
print(datetime(2020, 10, 10).strftime('%Y %B %d.'))
print(datetime(2022, 10, 28).isoformat())
print((datetime(2020, 10, 10) - datetime(2020, 5, 10)).days)

d = date(2022, 10, 28)
print(d)
t = time(12, 30)
print(t)
