import datetime
x = datetime.datetime.now()
print(x)
y = datetime.datetime.replace(x,x.year,x.month,x.day - 1,x.hour - 1,x.minute - 14 ,x.second,x.microsecond)
print(y)
t = datetime.datetime.timestamp(x) - datetime.datetime.timestamp(y)
t = round(t)
txt = "difference in seconds is {}"
print(txt.format((t)))