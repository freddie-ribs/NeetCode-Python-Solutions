class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Time: O(n)
        Space: O(1), since lookup table stores max 26 chars of alphabet
        '''
        seen = {}
        l = 0
        out = 0
        for r in range(len(s)):
            if s[r] not in seen:
                out = max(out, r - l + 1)
            else:
                if seen[s[r]] < l:
                    out = max(out, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return out
