class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        arrSum = sum(nums)
        if arrSum %2 != 0:
            return False

        target = arrSum/2

        def dfs(i, curSum):

            if curSum == target:
                return True

            if i >= len(nums):
                return True

            return dfs(i+1, curSum+nums[i]) or dfs(i+2, curSum+nums[i])

        return dfs(0, 0)

        
