class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Time: O(n logk)
        Space: O(n)
        '''
        h = []

        for x, y in points:
            dist = -(x*x + y*y)
            if len(h) == k:
                heapq.heappushpop(h, (dist, x, y))
            else:
                heapq.heappush(h, (dist, x, y))

        out = [(x, y) for (_, x, y) in h]
        return out
