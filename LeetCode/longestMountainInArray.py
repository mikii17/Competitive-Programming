class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        leftIndex = 0
        rightIndex = 1
        isMoun = False
        max_ = 0
        
        while rightIndex < len(arr):
            if arr[rightIndex] > arr[rightIndex - 1]:
                if isMoun:
                    max_ = max(max_, rightIndex - leftIndex)
                    leftIndex = rightIndex -1
                    isMoun = False
            elif arr[rightIndex] == arr[rightIndex - 1]:
                if isMoun and rightIndex - leftIndex > 1:
                    max_ = max(max_, rightIndex - leftIndex)
                    isMoun = False
                leftIndex = rightIndex
            else:
                if rightIndex - leftIndex < 2:
                    leftIndex = rightIndex
                else:
                    isMoun = True
            rightIndex += 1
        
        return max_ if not isMoun or max_ > rightIndex - leftIndex else rightIndex - leftIndex