string = "madam"
rstring = "".join(reversed(string))

print(rstring)
if string == rstring:
    print("PALINDROME")
else:
    print("NOT PALINDROME")