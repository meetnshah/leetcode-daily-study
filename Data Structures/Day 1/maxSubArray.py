def maxSubArray(nums):
#   Kadanes algorithm 
    maxIdx = nums[0]
    maxTotal = nums[0]
    for num in nums[1:]:
        maxIdx = max(num, maxIdx + num)
        maxTotal = max(maxIdx, maxTotal)
    return maxTotal

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))