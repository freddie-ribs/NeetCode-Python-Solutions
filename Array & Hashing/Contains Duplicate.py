class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''

    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in nums:
                d[n] = 1
            else:
                return True
        return False
