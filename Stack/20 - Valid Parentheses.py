class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        d = {"}": "{", ")": "(", "]": "["}
        stack = []

        for ch in s:
            if ch in d.values():
                stack.append(ch)
            else:
                if stack == [] or d[ch] != stack.pop():
                    return False
        return stack == []
