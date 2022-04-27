class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Time: O(nlogk)
        Space: O(k)
        '''
        h = nums[:k]
        heapq.heapify(h)
        for n in nums[k:]:
            heapq.heappush(h, n)
            heapq.heappop(h)
        return h[0]
