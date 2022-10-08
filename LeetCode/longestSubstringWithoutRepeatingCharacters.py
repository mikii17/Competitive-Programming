class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_ = {}
        leftIndex = 0
        output = ""
        
        for rightIndex in range(len(s)):
            while map_.get(s[rightIndex]):
                map_[s[leftIndex]] = None
                leftIndex += 1           
                
            map_[s[rightIndex]] = 1
            if len(output) < rightIndex - leftIndex + 1:
                output = s[leftIndex: rightIndex + 1]
                
        return len(output)
            
            