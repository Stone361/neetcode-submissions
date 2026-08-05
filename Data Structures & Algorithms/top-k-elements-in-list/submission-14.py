class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1

        minheap = []
        for n, c in mp.items():
            heapq.heappush(minheap, (c, n))
            if len(minheap)>k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
            