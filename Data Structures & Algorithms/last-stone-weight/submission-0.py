import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        # max heapify
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -abs(y-x))

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
            





        
            
        