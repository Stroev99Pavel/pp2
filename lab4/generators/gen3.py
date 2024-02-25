i = 0
n = 10
def Generator():
    global i
    global n
    while i < n:
        if i % 4 == 0 or i % 3 == 0:
            yield i
        i = i + 1
for x in Generator():
    print(x)