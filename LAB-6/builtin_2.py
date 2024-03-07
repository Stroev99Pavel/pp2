str = "CakeIslanD"
low_count = 0
up_count = 0
for x in str:
    if x.islower():
        low_count = low_count + 1
    if x.isupper():
        up_count = up_count +1
print(f"Total amount of lower case letter is {low_count}" )
print(f"Total amount of upper case letter is {up_count}")