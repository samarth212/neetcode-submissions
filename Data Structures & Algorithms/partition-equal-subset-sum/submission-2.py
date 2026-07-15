class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        arrSum = sum(nums)
        if arrSum %2 != 0:
            return False

        target = arrSum/2

        def dfs(i, curSum):
            

            if curSum == target:
                return True

            if curSum > target:
                return False

            if i >= len(nums):
                return False

            for j in range(i+1, len(nums)):
                if dfs(j, curSum+nums[j]):
                    return True

            return False
            

        return dfs(0, 0)

        
