class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [point[0]**2 + point[1]**2 for point in points]
        self.divide(distance, points)
        return points[:k]

    def divide(self, arr1, arr2):
        if len(arr1) < 2:
            return arr1, arr2

        mid = len(arr1) // 2
        left1, left2 = self.divide(arr1[:mid], arr2[:mid])
        right1, right2 = self.divide(arr1[mid:], arr2[mid:])
        self.conquer(arr1, left1, right1, arr2, left2, right2)
        
        return arr1, arr2

    def conquer(self, arr1, left1, right1, arr2, left2, right2):
        i = 0
        j = 0
        k = 0

        while i < len(left1) and j < len(right1):
            if left1[i] < right1[j]:
                arr1[k] = left1[i]
                arr2[k] = left2[i]
                i += 1
            else:
                arr1[k] = right1[j]
                arr2[k] = right2[j]
                j += 1
            k += 1
        
        while i < len(left1):
            arr1[k] = left1[i]
            arr2[k] = left2[i]
            i += 1
            k += 1
        
        while j < len(right1):
            arr1[k] = right1[j]
            arr2[k] = right2[j]
            j += 1
            k += 1
