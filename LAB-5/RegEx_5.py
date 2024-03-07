import re
str1 = "adsb"
str2 = "a_no_one_b"
str3 = "123abo_abob_leab"
print(re.findall("a.+b$",str1))
print(re.findall("a.+b$",str2))
print(re.findall("a.+b$",str3))