class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = 0
        sum_ = 0

        while j - i < k:
            sum_ += nums[j]
            j += 1
        max_ = sum_
        while j < len(nums):
            sum_ = sum_ - nums[i] + nums[j]
            max_ = max(max_, sum_)
            i += 1
            j += 1
        
        return max_ / k
