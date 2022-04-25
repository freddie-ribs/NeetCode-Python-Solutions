class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Time: O(n)
        Space: O(1)
        '''
        out = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            out[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= postfix
            postfix *= nums[i]
        return out
