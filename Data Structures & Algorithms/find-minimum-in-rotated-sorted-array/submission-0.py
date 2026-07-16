class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] < nums[-1]:
            return nums[0]
        
        minn = nums[-1]
        l = 0
        r = len(nums) - 1
        m = None
        while l < r:
            m = (l + r)//2
            if nums[m] < nums[l]:
                r = m
            elif nums[m] > nums[l]:
                l = m
            
            if r == m:
                return nums[m]
        return nums[m]

        