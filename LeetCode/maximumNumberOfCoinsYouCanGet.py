class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        numCoins = 0

        i = 0
        while i < len(piles) // 3:
            numCoins += piles[2*i + 1]
            i += 1
        
        return numCoins
