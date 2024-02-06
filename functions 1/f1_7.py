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
nums1 = [1, 3, 3, 3]
nums2 = [1, 1, 1, 1]
nums3 = [1, 3, 1, 3]
print(has_33(nums1))
print(has_33(nums2))
print(has_33(nums3))