import re
str1 = "lemon_lime_Garlic_who"
new = re.split("_",str1)
print(new)
lenght = len(new)
i = 1
new[0] = new[0].lower()
str2 = new[0]
while i<lenght:
    time = new[i]
    time = time.capitalize()
    str2 = str2 + time
    i = i + 1
print(str2)