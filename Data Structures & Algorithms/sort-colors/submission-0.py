class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
                l
        [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
                           r

        have apointer l and r, l = 0 and r = n-1
        represnets the next location a 0 or 2 should go

        loop through array, if we see a 0, swap it with l, and adance 1
        if we see a 2: while arr[i] is still 2, continue swapping and reducing r

        we return when we reach a 2 that is >= r
        """

        l = 0
        r = len(nums) - 1

        for i in range(len(nums)):

            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            
            if nums[i] == 2:
                if i >= r:
                    break
                while nums[i] == 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r -=1
            
            
















        