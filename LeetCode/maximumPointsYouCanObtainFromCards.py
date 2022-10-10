class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_ = 0
        mSum = 0
        minSum = float('inf')
        k = len(cardPoints) - k
         
        for i in range(len(cardPoints)):
            sum_ += cardPoints[i]
            
            if i + 1 > k:
                mSum = mSum - cardPoints[i - k] + cardPoints[i]
                minSum = min(minSum, mSum)
            else:
                mSum += cardPoints[i]
                if i + 1 == k:
                    minSum = min(minSum, mSum)
        
        return sum_ - minSum
            
        
        