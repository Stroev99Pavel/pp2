N = 10
i = 1
def Generator():
    global i
    global N
    while(i < N):
        yield i*i
        i = i + 1
for x in Generator():
    print(x)