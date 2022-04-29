class Solution(object):
    def maxArea(self, height):
        '''
        Time: O(n)
        Space: O(1)
        '''
        l, r = 0, len(height) - 1
        out = 0

        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            out = max(cur, out)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return out
