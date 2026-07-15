class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) == 1:
            return 0

        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                prevEnd = min(interval[1], prevEnd)
                res+=1

        return res

            

        