class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            j = i
            current = nums[j]
            while j > 0 and nums[j] + nums[j - 1] > nums[j - 1] + nums[j]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1  
        
        ans = "".join(nums)
        return str(int(ans))
        