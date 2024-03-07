import re
str = "LuffyZoroNamiUsoppSanji"
#new = re.split("[A-Z]",str)
new = re.findall("[A-Z]+[a-z]+",str)
print(new)