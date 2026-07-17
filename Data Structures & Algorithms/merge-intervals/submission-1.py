class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        new = [intervals[0]]
        for i in range(1, len(intervals)):
            interval1 = new[-1]
            interval2 = intervals[i]

            if interval1[1] < interval2[0]:
                new.append(interval2)
            else:
                newInterval = [
                    min(interval1[0], interval2[0]), 
                    max(interval1[1], interval2[1])
                ]
                new[-1] = newInterval
        
        return new





            

