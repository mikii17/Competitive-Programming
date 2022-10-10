class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            if leftSum == sum_ - leftSum - nums[i]:
                return i
            leftSum += nums[i]
        
        return -1