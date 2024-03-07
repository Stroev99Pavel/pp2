import os
with open("Strawhats.txt", 'r') as file:
    ans = sum(1 for line in file)
print(ans)
