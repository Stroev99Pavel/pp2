import re
str1 = "GAINPain"
str2 = "lower"
str3 = "AndroidBossGameBOX"
print(re.findall("[A-Z][a-z]+[a-z]",str1))
print(re.findall("[A-Z][a-z]+[a-z]",str2))
print(re.findall("[A-Z][a-z]+[a-z]",str3))