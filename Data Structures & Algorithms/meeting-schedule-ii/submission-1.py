"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 1:
            return 1

        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        print(start)
        print(end)

        count = 0
        i = 0
        j = 0
        while i < len(start)-1:
            if start[i] < end[j]:
                count +=1
                i +=1
            else:
                count -=1
                j +=1



        return count
