class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        minheap = []
        for n, c in cnt.items():
            heapq.heappush(minheap, (c, n))
            if len(minheap)>k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
            