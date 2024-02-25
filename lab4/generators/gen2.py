n = input()
n = int(n)
i = 0
def Generator():
    global i
    global n
    while i < n:
        yield i
        i = i + 1
ev = []
for x in Generator():
    if x % 2 == 0:
        ev.append(x)
print(ev)
