class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # loop through the array, at each step we can choose to pop or skip
        # if we pop, we then want the max from that point, passing in the new array
        # dfs(remaining):
            # base case: when remining is empty
            # remaining is calclated by nums[:i] + nums[i+1::]
            # loop through remaining and try popping each one

        
        def burst(i, remaining):
            prev = remaining[i-1] if i-1 >= 0 else 1
            nxt = remaining[i+1] if i+1 < len(remaining) else 1
            return prev * remaining[i] * nxt
      

        dp = {}

        def dfs(remaining):
            best = 0

            if not remaining:
                return 0

            if tuple(remaining) in dp:
                return dp[tuple(remaining)]

            
            for i in range(len(remaining)):

                coins = burst(i, remaining)
                best = max(coins + dfs(remaining[:i] + remaining[i+1::]), best)
            
            dp[tuple(remaining)] = best
            return best
       
        
        return dfs(nums)
        

        





        