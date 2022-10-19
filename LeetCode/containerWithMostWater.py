class Solution:
    def maxArea(self, height: List[int]) -> int:
        rightIndex  = len(height) - 1
        leftIndex = 0
        maxArea = 0
        
        while leftIndex < rightIndex:
            if height[leftIndex] <= height[rightIndex]:
                maxArea = max(maxArea, height[leftIndex] * (rightIndex - leftIndex))
                leftIndex += 1
            else:
                maxArea = max(maxArea, height[rightIndex] * (rightIndex - leftIndex))
                rightIndex -= 1
        
        return maxArea