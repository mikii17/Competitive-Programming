class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0] * len(nums)
        
        for i in range(len(nums)):
            for num in nums:
                if num < nums[i]:
                    output[i] += 1
        return output