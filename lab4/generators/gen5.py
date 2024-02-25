i = 0
n = 11
def Generator():
    global i
    global n
    while (n > i):
        yield n
        n = n - 1
for x in Generator():
    print(x)