class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [float("inf")] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i] != float("inf"):
                return dp[i]

            res = cost[i] + min(dfs(i+1), dfs(i+2))
            dp[i] = res
            return res

        return min(dfs(0), dfs(1))

        