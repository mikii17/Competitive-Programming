class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxNum = 0
        map_ = {}
        leftIndex = 0
        
        for i in range(len(fruits)):
            if fruits[i] in map_ or len(map_) < 2:
                map_[fruits[i]] = i
                
            else:
                minKey = self._minKey(map_)
                leftIndex = map_.pop(minKey) + 1
                map_[fruits[i]] = i
                
            maxNum = max(maxNum, i - leftIndex + 1)
        return maxNum
    
    def _minKey(self, map_):
        minVal = float("inf")
        minKey = 0
        
        for key, val in map_.items():
            if val < minVal:
                minVal = val
                minKey = key
        
        return minKey