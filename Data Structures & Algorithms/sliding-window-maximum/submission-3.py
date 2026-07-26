class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''

        first window is 0:k
        store a max heap of size k

        for every new r, add the new element and remove old
        peek max, append

        l = r - k + 1

        '''

        heap = []
        for i in range(0, k):
            heap.append( (-nums[i], i) )
        
        heapq.heapify(heap)
        res = [-heap[0][0]]

        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            left = r - k + 1

            while heap[0][1] < left:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            
        return res




        
        