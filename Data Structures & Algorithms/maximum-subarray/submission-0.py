class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        best = nums[0]

        curSum = best

        for i in nums[1:]:
            add = curSum + i
            if add >= i:
                curSum += i
            else:
                curSum = i

            
            best = max(best, curSum)

        return best
        
