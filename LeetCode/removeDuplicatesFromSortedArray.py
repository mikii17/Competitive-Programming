class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        left = 0
        right = 1

        while right < len(nums):
            if nums[right] == nums[left]:
                right += 1
            else:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                left += 1
                right += 1
        print(nums)
        return left + 1
