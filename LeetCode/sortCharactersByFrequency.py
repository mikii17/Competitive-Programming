class Solution:
    def frequencySort(self, s: str) -> str:
        map_ = {}

        for char in s:
            map_[char] = map_[char] + 1 if map_.get(char) else 1
        
        sortedChar = sorted(map_.keys(), key=lambda x: map_[x], reverse=True)
        ans = ''
        for char in sortedChar:
            ans += char * map_[char]
        
        return ans
