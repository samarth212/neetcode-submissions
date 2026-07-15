class Solution:
    # bottom up 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) #init dp aray with defualt unreachable value (amount + 1)
        dp[0] = 0 # init what we know

        for a in range(1, amount+1):
            for coin in coins:
                #if we can validly use this coin
                if (a-coin) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]


        