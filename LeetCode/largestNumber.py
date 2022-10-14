class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums[0] = str(nums[0])
        for i in range(1, len(nums)):
            nums[i] = str(nums[i])
            key = nums[i]
            j = i - 1

            while j >= 0 and int(key + nums[j]) > int(nums[j] + key):
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j -= 1

        return str(int("".join(nums)))