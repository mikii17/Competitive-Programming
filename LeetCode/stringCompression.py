class Solution:
    def compress(self, chars: List[str]) -> int:
        output = chars.copy()
        chars.clear()
        lt =  0
        
        for i in range(len(output) + 1):
            
            if i == len(output) or output[i] != output[lt]:
                chars.append(output[lt])
                dif = str(i - lt) if i - lt > 1 else ""
                j = 0
                while j < len(dif):
                    chars.append(dif[j])
                    j += 1
                lt = i

            