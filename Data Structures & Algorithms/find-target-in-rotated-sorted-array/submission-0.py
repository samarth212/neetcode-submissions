class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findStart(nums):

            if nums[0] < nums[-1]:
                return 0
            
            l = 0
            r = len(nums) - 1
            while l < r:
                m = (l + r)//2
            
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
                
                
            return l

        
        def searchTarget(nums, target):

            l = 0
            r = len(nums)-1

            while l <= r:
                m = (l+r)//2

                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    l = m+1
                else:
                    r = m-1

            return -1


        start = findStart(nums)

        #0:start
        #start:len(nums)

        res1 = searchTarget(nums[0:start], target)
        res2 = searchTarget(nums[start:len(nums)], target)
        if res2 != -1:
            res2+=start
        return max(res1, res2)


        