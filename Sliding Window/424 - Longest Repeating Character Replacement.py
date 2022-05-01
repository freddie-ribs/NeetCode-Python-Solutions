class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time: O(n)
        Space: O(1)
        '''
        l = 0
        d = Counter()
        freq = 0
        for r in range(len(s)):
            d[s[r]] += 1
            freq = max(freq, d[s[r]])
            if r - l + 1 > freq + k:
                d[s[l]] -= 1
                l += 1
        return r - l + 1
