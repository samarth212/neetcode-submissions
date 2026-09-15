class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # [1,3],[2,3],[3,7],[6,6]
        # [3].  [2].  [5].  [1]    

        res = []

        for j in queries:
            best = float('inf')
            for i in range(len(intervals)):
                if intervals[i][0] <= j <= intervals[i][1]:
                    best = min(best, intervals[i][1]-intervals[i][0]+1)
            if best == float('inf'):
                res.append(-1)
            else:
                res.append(best)

        return res



            