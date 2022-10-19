class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        score = 0
        lt, rt = 0, len(tokens) - 1
        tokens.sort()
        
        while lt <= rt:
            if tokens[lt] <= power:
                score += 1
                power -= tokens[lt] 
                lt += 1
            else:
                if lt == rt or score == 0:
                    break
                score -= 1
                power += tokens[rt]
                rt -= 1
        
        return score
print(Solution().bagOfTokensScore([100,200],150))