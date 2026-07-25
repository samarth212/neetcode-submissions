class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        '''
        for each possible start, we consider every additioal step
        at each step, we can either choose greater num or skip

        dfs(i)
        - base case: if i is the end, return 1

        - loop through remaining js
        - best
        - if j > i -> best = max(best, 1 + dfs(j))

        '''

        dp = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 1

            if i in dp:
                return dp[i]

            best = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1+dfs(j))
            
            dp[i] = best
            return dp[i]

        best = 1
        for i in range(len(nums)):
            best = max(best, dfs(i))

        return best

        



        