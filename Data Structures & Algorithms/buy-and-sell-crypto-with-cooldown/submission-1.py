class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''

        dfs(i, profit)
        base case: i reached end: compare to local best to best

        at every i , loop through everyting ahead
            we calculate our profit, and pass it in to i+2
            update local best from i

        '''

        res = 0
        dp = {}

        def dfs(i):
            nonlocal res 

            if i >= len(prices):
                return 0

            if i in dp:
                return dp[i]

            best = dfs(i+1)
            for j in range(i+1, len(prices)):

                newProfit = prices[j]-prices[i]
                best = max(best, newProfit + dfs(j+2))

            dp[i] = best          
            return best
            
        return dfs(0)

        
        