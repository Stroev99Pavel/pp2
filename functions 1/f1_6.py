def reverse(s):
    reversed = ""
    listS = []
    lenght = len(s)
    i = 0
    new = ""
    while i < lenght:
        if s[i] != " ":
            new = new + s[i]
        else:
            listS.insert(0,new)
            new = ""
        i = i + 1
    listS.insert(0, new)
    i = 0
    while i < len(listS):
        reversed = reversed + listS[i] + " "
        i = i + 1
    return reversed
str = "Algebra Math Geometry Game"
print(reverse(str))