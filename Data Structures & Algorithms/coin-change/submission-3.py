class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        '''
        [1,5,10], amount = 12

        dfs(remaining) -> return depth 
         - base cases: remaining = 0, < 0

        dfs(12) = min(dfs(11), dfs(7), dfs(2))

        loop through choices
        run dfs(amount-choice = remaining)
            if remaining = 0, return 1
            if remaining < 0, return infinity

            return 1 + min(remaining choices)

        return dfs(amount)

        '''
        
        def dfs(remaining):

            if remaining == 0:
                return 1
            if remaining < 0:
                return float('inf')

            minDepth = float('inf')
            for i in coins:
                minDepth = min(dfs(remaining-i), minDepth)

            return 1 + minDepth

        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res - 1

       