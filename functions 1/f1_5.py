
from itertools import permutations
def ST(s):
    p = permutations(s)
    for x in list(p):
        print(x)
str = input()
ST(str)