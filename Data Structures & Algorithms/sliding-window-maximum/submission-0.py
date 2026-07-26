class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        '''

        first window is 0:k
        get max from that, prevMax, add to output
            output array
        
        r, l = r-k+1

        prevL

        does losing prevL or gaining newR change prevMax?

        if newL = prevMax

        '''

        res = []
        for r in range(k-1, len(nums)):
            l = r-k+1
            res.append(max(nums[l:r+1]))
        
        return res


        