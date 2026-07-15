import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = [] # for the right side
        self.maxheap = [] # for the left side 

        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        # rebalance by pushing the right into left if right is bigger
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

            
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return float(-self.maxheap[0])
        return float((-self.maxheap[0] + self.minheap[0])/2)
        