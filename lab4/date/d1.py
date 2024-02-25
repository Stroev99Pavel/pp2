import datetime
x = datetime.datetime.now()
#print(x.strftime("%d"))
print(x)
x = datetime.datetime.replace(x,x.year, x.month, x.day - 5)
print(x)