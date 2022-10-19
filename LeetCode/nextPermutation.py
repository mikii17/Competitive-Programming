class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftPointer = len(nums) - 2
        min_ = -1
        
        while min_ == -1 and leftPointer >= 0:
            rightPointer = leftPointer + 1
            
            while rightPointer < len(nums):
                if nums[leftPointer] < nums[rightPointer]:
                    min_ = rightPointer if min_ == -1 or nums[min_] > nums[rightPointer] else min_ 
                
                rightPointer += 1
            
            leftPointer -= 1
        
        if min_ == -1:
            nums.sort()
        else:
            nums[leftPointer + 1], nums[min_] = nums[min_], nums[leftPointer + 1]
            
            for i in range(leftPointer + 3, len(nums)):
                j = i - 1
                while j >= leftPointer + 2 and nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j -= 1
                    