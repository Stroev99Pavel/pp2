def palindrome(s):
    str = ""
    i = len(s) - 1
    while i != 0:
        str = str + s[i]
        i = i - 1
    str = str + s[0]
    if str == s:
        return True
    else:
        return False

print(palindrome("madam"))
print(palindrome("LoL"))
print(palindrome("Kanye"))