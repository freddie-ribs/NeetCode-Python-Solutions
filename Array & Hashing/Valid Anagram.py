class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Time: O(n)
                Space: O(1)
        '''
        d = {}

        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

        for ch in t:
            if ch in d:
                d[ch] -= 1
                if d[ch] < 0:
                    return False
            else:
                return False

        for val in d.values():
            if val > 0:
                return False

        return True
