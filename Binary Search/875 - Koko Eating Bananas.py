class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Time: O(n logm)
        Space: O(1)
        '''
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += ceil(p / m)
            if hours > h:
                l = m+1
            else:
                r = m
        return r
