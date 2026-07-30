class Solution:
    def jump(self, nums: List[int]) -> int:

        '''
                 r 
        [2,4,1,1,1,1]
                   l

               l
        [2,1,2,1,0]
                 r

        '''

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            best = 0
            for i in range(l, r+1): 
                best = max(best, i + nums[i])
            l = r + 1
            r = best
            res += 1
        
        return res





        
        