class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_ = {}
        leftIndex = 0
        output = 0
        
        for rightIndex in range(len(s)):
            if s[rightIndex] in map_ and leftIndex <= map_.get(s[rightIndex]):
                leftIndex = map_.get(s[rightIndex]) + 1
                
            map_[s[rightIndex]] = rightIndex
            output = max(output, rightIndex - leftIndex + 1)
                
        return output
            
