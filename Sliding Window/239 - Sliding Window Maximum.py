class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Time: O(n)
        Space: O(k), size of k window
        '''
        dq = deque([])
        out = []

        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i + 1 >= k:
                out.append(nums[dq[0]])
            if i - dq[0] + 1 >= k:
                dq.popleft()
        return out
