class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # [1,3],[2,3],[3,7],[6,6]
        # [3].  [2].  [5].  [1]

        intervals.sort()
        heap = []
        res = {}
        i = 0

        for j in sorted(queries): 
            while i < len(intervals) and intervals[i][0] <= j:
                l, r = intervals[i]
                heapq.heappush(heap, (r-l+1, r))
                i+=1

            while heap and heap[0][1] < j:
                heapq.heappop(heap)

            res[j] = heap[0][0] if heap else -1


        return [res[j] for j in queries]           




     




            