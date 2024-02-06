def Volume(R):
    return R*R*R*3.14*(4/3)
def convert(grams):
    print(grams * 28.3495231)
def has_33(nums):
    lenght = len(nums)
    i = 0
    count = 0
    while i < lenght - 1:
        if nums[i] == 3 and nums[i+1] == 3:
            count = 1
        i = i + 1
    if count == 1:
        return True
    else:
        return False
def histogram(lists):
    lenght = len(lists)
    i = 0
    while i < lenght:
        j = 0
        while j < lists[i]:
            print("*",end="")
            j = j + 1
        print("")
        i = i + 1

print("Radius?")
Rad = input()
print(Volume(int(Rad)))
print("Grams?")
G = input()
convert(int(G))
print(has_33([1,2,3,4,0,1,0,3,4,5,7]))
print(has_33([1,2,3,4,0,1,0,3,3,3,7]))
histogram([1,2,3,4,5,5,4,3,2,1])