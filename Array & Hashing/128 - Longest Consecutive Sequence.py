class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        numset = set(nums)
        best = 0
        for n in nums:
            if (n - 1) not in numset:
                cur = 0
                while n + cur in numset:
                    cur += 1
                best = max(cur, best)

        return best
