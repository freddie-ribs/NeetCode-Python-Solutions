class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        cur, best = 0, 0
        for i in range(1, len(prices)):
            cur = max(cur + (prices[i] - prices[i - 1]), 0)
            best = max(best, cur)
        return best
