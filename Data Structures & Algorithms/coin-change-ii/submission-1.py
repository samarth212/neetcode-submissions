class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        '''

        keep frequency count to track dups

        backtrack and treat freq as the path

        dfs(target)
        - base case: target = 0, increase total
        - target < 0, return 

        for i in coins, if the diff >= 0, run dfs on diff

        '''

        dp = {}

        def dfs(i, target):
            if target == 0:
                return 1

            if (i, target) in dp:
                return dp[(i, target)]

            ways = 0

            for j in range(i, len(coins)):
                if coins[j] <= target:
                    ways += dfs(j, target-coins[j])

            dp[(i, target)] = ways
            return ways

        return dfs(0, amount)