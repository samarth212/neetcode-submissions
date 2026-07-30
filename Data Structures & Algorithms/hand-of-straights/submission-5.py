class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        
        if len(hand)%groupSize != 0:
            return False

        freq = defaultdict(int)
        for i in hand:
            freq[i] += 1

        heap = list(freq.keys())
        heapq.heapify(heap)
        while heap:
            n = heap[0]

            for i in range(n, n+groupSize):
                if i not in freq:
                    return False
                freq[i] -=1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True
        