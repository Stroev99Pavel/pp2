import re
str = "longRingLandArc"
new = re.findall("[a-z]+[a-z]|[A-Z]+[a-z]+",str)
i = 1
ans = new[0]
while i < len(new):
    ans = ans + "_"+ new[i]
    i = i + 1
print(ans)