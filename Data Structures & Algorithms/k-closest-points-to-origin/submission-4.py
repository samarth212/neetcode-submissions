class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (-d, [x, y]))
            else:
                if d < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-d, [x, y]))

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return res