def spy_game(nums):
    lenght = len(nums)
    i = 0
    count = 0
    while i < lenght:
        if count == 0 and nums[i] == 0:
            count = 1
        if count == 1 and nums[i] == 0:
            count = 2
        if count == 2 and nums[i] == 7:
            count = 3
        i = i + 1
    if count == 3:
        print("True")
    else:
        print("False")
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
spy_game([0,1,7,0,7])