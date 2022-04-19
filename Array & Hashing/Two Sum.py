class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
                Time: O(n)
                Space: O(n)
                '''
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            else:
                d[num] = i
