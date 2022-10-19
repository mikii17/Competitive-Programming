class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        output = 0
        for i in range(len(arr)):
            hashMap = {}
            for j in range(i+1, len(arr)):
                temp = arr[i] + arr[j]
                if target - temp in hashMap:
                    output += hashMap[target - temp]
            
                hashMap[arr[j]] = hashMap[arr[j]] + 1 if hashMap.get(arr[j]) else 1
        
        return output %  (10 ** 9 + 7)