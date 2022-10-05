class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1

        min = self.binarySearch(nums,target)
        if (min == -1):
            return []
        else:
            max = min
            while True:
                if min <= 0:
                    break
                if nums[min - 1] == target:
                    min = min - 1
                else:
                    break

            while True:
                if max >= len(nums) - 1:
                    break
                if nums[max + 1] == target:
                    max = max + 1
                else:
                    break
            output = [i for i in range(min, max + 1)]

            return output

    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1