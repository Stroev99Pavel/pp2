import datetime
x = datetime.datetime.now()
y = datetime.datetime.replace(x,x.year,x.month,x.day,x.hour,x.minute,x.second,0)
#print(x.strftime("%d"))
print(x)
micro = x.strftime("%f")
print(y)
