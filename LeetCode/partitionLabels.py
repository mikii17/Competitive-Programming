class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        
        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]][1] = i
            else:
                hashMap[s[i]] = [i, i]
        
        output = []
        lt = 0
        lastIndex = 0
        
        print(hashMap)
        while lt < len(s):
            if not output or hashMap[s[lt]][0] == lastIndex + 1:
                output.append(hashMap[s[lt]][1] - hashMap[s[lt]][0] + 1)
                lastIndex = hashMap[s[lt]][1]
            elif hashMap[s[lt]][1] > lastIndex:
                output[-1] += hashMap[s[lt]][1] - lastIndex
                lastIndex += hashMap[s[lt]][1] - lastIndex
            lt += 1
        return output