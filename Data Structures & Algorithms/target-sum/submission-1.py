class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        '''

        dfs(i, amount)
        - once we reach end, if amount = target, return 1
        - else if at the end return 0

        return dfs(i+1, amount-nums[i]) + dfs(i+1, amount+nums[i])

        '''

        dp = {}

        def dfs(i, amount):
            if i == len(nums):
                return 1 if amount == 0 else 0

            if (i, amount) in dp: 
                return dp[(i, amount)]

            dp[(i, amount)] = dfs(i+1, amount-nums[i]) + dfs(i+1, amount+nums[i])
            return dp[(i, amount)]


        return dfs(0, target)
        