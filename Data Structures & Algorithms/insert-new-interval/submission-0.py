class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                new.append(newInterval)
                return new + intervals[i:]
            if newInterval[0] > interval[1]:
                new.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        
        new.append(newInterval)
        return new

                
        