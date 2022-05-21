class Solution(object):
    def search(self, nums, t):
        '''
        Time: O(logn)
        Space: O(1)
        '''
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == t:
                return mid
            if nums[l] <= nums[mid]:
                if t < nums[l] or t > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if t < nums[mid] or t > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
