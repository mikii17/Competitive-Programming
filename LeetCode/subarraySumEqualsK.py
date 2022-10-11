class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = {}
        prefixSum = 0
        result = 0
        
        for num in nums:
            prefixSum += num
            if prefixSum == k:
                result += 1
            
            if (prefixSum - k) in prefixSumMap:
                result += prefixSumMap[prefixSum - k]
            
            if prefixSum in prefixSumMap:
                prefixSumMap[prefixSum] += 1
            else:
                prefixSumMap[prefixSum] = 1
        
        return result
                
            