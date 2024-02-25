import datetime
x = datetime.datetime.now()
yesterday = datetime.datetime.replace(x,x.year,x.month,x.day - 1 )
tomorrow = datetime.datetime.replace(x,x.year,x.month,x.day + 1)
#print(x.strftime("%d"))
print(yesterday)
print(x)
print(tomorrow)
