class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.divide(intervals)
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1] = [output[-1][0], max(intervals[i][1], output[-1][1])]
            else:
                output.append(intervals[i])

        return output
    
    def divide(self, arr):
        if len(arr) < 2:
            return arr

        mid = len(arr) // 2
        left = self.divide(arr[:mid])
        right = self.divide(arr[mid:])
        self.conquer(arr, left, right)
        
        return arr

    def conquer(self, arr, left, right):
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


