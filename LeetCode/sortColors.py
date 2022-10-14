class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZero = -1
        lastOne = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                lastZero += 1
                lastOne += 1
                nums[lastZero], nums[i] = nums[i], nums[lastZero]
                if nums[i] == 1:
                    nums[lastOne], nums[i] = nums[i], nums[lastOne]
            elif nums[i] == 1:
                lastOne += 1
                nums[lastOne], nums[i] = nums[i], nums[lastOne]