i = 0
a = 4
b = 12
def squares():
    global a
    global b
    while a < b:
        yield a*a
        a = a + 1
for x in squares():
    print(x)