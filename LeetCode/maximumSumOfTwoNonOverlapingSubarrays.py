class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        firstSum = 0
        secondSum = 0
        maxSum = 0
        
        for i in range(len(nums) + 1):
            if i + 1 <= firstLen:
                firstSum += nums[i]
            else:
                if i - firstLen >= secondLen:
                    secondSum = 0
                    for j in range(i - firstLen):
                        if j + 1 <= secondLen:
                            secondSum += nums[j]
                            if j + 1 == secondLen:
                                maxSum = max(maxSum, firstSum + secondSum)
                        else:
                            secondSum = secondSum + nums[j] - nums[j -secondLen]  
                            maxSum = max(maxSum, firstSum + secondSum)
                if len(nums) - i >= secondLen:
                    secondSum = 0
                    for j in range(len(nums) - i):
                        if j + 1 <= secondLen:
                            secondSum += nums[i + j]
                            if j + 1 == secondLen:
                                maxSum = max(maxSum, firstSum + secondSum)
                        else:
                            secondSum = secondSum + nums[j + i] - nums[j + i - secondLen]
                            maxSum = max(maxSum, firstSum + secondSum)
                if i < len(nums):
                    firstSum = firstSum + nums[i] - nums[i - firstLen]

            
                    
        return maxSum
