class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            ways = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                ways += dfs(i+2)

            dp[i] = ways
            return dp[i]
            
        return dfs(0)
          