class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return nums[0]

        # at all times we have 2 choices; either include 
        # the next element or start again at the next element

        curSum = best = nums[0]

        for i in range(1, len(nums)):
            temp = curSum + nums[i]

            if temp >= nums[i]:
                curSum += nums[i]
            else:
                curSum = nums[i]

            best = max(best, curSum)


        return best


        