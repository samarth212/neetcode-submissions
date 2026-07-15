class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort intervals
        # add first interval to output
        # loop through starting from second
        # if overlap, replace last item in output with min and max
        # if not, append to output

        if len(intervals) == 1:
            return intervals


        intervals.sort()

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if output[-1][1] >= interval[0]:
                output[-1] = [min(output[-1][0],interval[0]), max(interval[1], output[-1][1])]
            else:
                output.append(interval)

        return output




        
        