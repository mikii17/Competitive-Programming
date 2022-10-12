class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        map_ = {0:1}
        output = 0
        prefixSum = 0

        for num in nums:
            if num % 2 == 1:
                prefixSum += 1
            
            if prefixSum - k in map_:
                output += map_[prefixSum - k]
            
            if prefixSum in map_:
                map_[prefixSum] += 1
            else:
                map_[prefixSum] = 1

        return output 