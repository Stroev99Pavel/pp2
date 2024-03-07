import re
str = "LuffyZoroNamiUsoppSanji"
#new = re.split("[A-Z]",str)
new = re.findall("[A-Z]+[a-z]+",str)
ans = new[0]
i = 1
while i < len(new):
    ans = ans + " " + new[i]
    i = i + 1
print(ans)