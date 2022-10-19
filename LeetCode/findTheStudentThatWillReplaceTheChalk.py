class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_ = sum(chalk)
        k = k % sum_
        i = 0
        psum = 0
        
        while k - psum >= chalk[i]:
            psum += chalk[i]
            i = (i + 1) % len(chalk)
        
        return i