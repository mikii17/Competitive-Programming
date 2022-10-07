class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxNum = 0
        leftIndex = 0
        flippedZeros = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                maxNum = max(maxNum, i - leftIndex + 1)
            elif flippedZeros < k:
                maxNum = max(maxNum, i - leftIndex + 1)
                flippedZeros += 1
            else:
                if nums[leftIndex] == 0:
                    leftIndex += 1
                else:
                    leftIndex += 1
                    while nums[leftIndex] != 0:
                        leftIndex += 1
                    leftIndex += 1
        return maxNum
                    