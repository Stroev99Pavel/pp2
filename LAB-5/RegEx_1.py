import re

str1 = "abbbbb"
str2 = "a"
str3 = "ab"

print(re.findall("ab*",str1))
print(re.findall("ab*",str2))
print(re.findall("ab*",str3))
