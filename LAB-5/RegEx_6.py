import re
str1 = "...1..."
str2 = "      "
str3 = ".,. 13"
print(re.sub("[,]|[.]|[\s]",":", str1))
print(re.sub("[,]|[.]|[\s]",":", str2))
print(re.sub("[,]|[.]|[\s]",":", str3))




