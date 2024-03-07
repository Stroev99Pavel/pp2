import re

str1 = "abbbbb"
str2 = "aabbb"
str3 = "aaa"

print(re.findall("ab{2}|ab{3}",str1))
print(re.findall("ab{2}|ab{3}",str2))
print(re.findall("ab{2}|ab{3}",str3))
