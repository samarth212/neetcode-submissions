class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
         l
        [1, 0, 2]
               r

        have apointer l and r, l = 0 and r = n-1
        represnets the next location a 0 or 2 should go

        loop through array, if we see a 0, swap it with l, and adance 1
        if we see a 2: while arr[i] is still 2, continue swapping and reducing r

        we return when we reach a 2 that is >= r
        """

        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:

            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                
                if i >= r:
                    break
         
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            
            else: i += 1

            
            
















        