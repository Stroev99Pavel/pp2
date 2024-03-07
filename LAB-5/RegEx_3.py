import re
str1 = "a_b_c_dad_sdsd_ded__"
str2 = "A_B_ABC_DXE"
str3 = "ab_cd"
print(re.findall("[a-z]+[_][a-z]+",str1))
print(re.findall("[a-z]+[_][a-z]+",str2))
print(re.findall("[a-z]+[_][a-z]+",str3))