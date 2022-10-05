class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(2):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums[index], nums[j] = nums[j], nums[index]
                    index += 1
                    
            
        