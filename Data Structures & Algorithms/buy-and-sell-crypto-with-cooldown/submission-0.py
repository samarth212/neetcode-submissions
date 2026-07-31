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

        def dfs(i, profit):
            nonlocal res 

            if i >= len(prices):
                return profit

            best = dfs(i+1, profit)
            for j in range(i+1, len(prices)):
                newProfit = prices[j]-prices[i] + profit
                best = max(best, dfs(j+2, newProfit))
            
            return best
            
                

        return dfs(0, 0)

        
        