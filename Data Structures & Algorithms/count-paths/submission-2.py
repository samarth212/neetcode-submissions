class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        for bottom up start at the end

        dp[m-1][r-1] = 1 -> base
        dp[m][x] = 0 -> base
        dp[x][n] = 0 -> base

        dp[m-1][r-2] = dp[m-1][r-1] + dp[m][r-2] = 1
        dp[m-1][r-3] = dp[m-1][r-1] + etc. 

        '''

        
        dp = [[-1] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(n+1):
            dp[m][i] = 0
        for i in range(m+1):
            dp[i][n] = 0

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue

                dp[r][c] = dp[r][c+1] + dp[r+1][c]

        return dp[0][0]

                

        