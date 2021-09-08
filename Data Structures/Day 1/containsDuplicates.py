def containsDuplicate(nums):
    dict = {}
    for i in nums:
        if nums[i] in dict:
            return True
        else:
            dict[nums[i]] = 1
    return False
    # return len(nums) != len(set(nums))

print(containsDuplicate([[1,2,3,1]]))