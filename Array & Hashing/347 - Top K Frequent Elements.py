class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Time: O(n)
        Space: O(n)
        '''
        d = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in d.items():
            bucket[freq].append(num)

        out = []

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                out.append(num)
                if len(out) == k:
                    return out
