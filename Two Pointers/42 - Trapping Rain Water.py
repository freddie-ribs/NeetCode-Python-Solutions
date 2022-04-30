class Solution:
    def trap(self, h: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        if len(h) < 3:
            return 0
        out = 0
        maxL, maxR = h[0], h[len(h) - 1]
        l, r = 1, len(h) - 2
        while l <= r:
            if maxL < maxR:
                if h[l] > maxL:
                    maxL = h[l]
                else:
                    out += maxL - h[l]
                l += 1
            else:
                if h[r] > maxR:
                    maxR = h[r]
                else:
                    out += maxR - h[r]
                r -= 1
        return out
