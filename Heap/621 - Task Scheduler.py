class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Time: O(mn), where m is cool off period
        Space: O(1), max possible O(26), due to alpha chars of 
        '''
        h = []
        time = 0
        count = Counter(tasks)

        for key, val in count.items():
            heapq.heappush(h, (-val, key))

        while h:
            tmp = []
            i = 0
            while i <= n:
                time += 1
                if h:
                    val, key = heapq.heappop(h)
                    if val != -1:
                        tmp.append((val+1, key))
                if not h and not tmp:
                    break
                else:
                    i += 1
            for task in tmp:
                heapq.heappush(h, task)

        return time
