class Solution:
    def numDecodings(self, s: str) -> int:

        '''

        1012

        dp[3] = 1 -> base case
        dp[2] = 1 + dp[3] = 2
        dp[1] = 0 + dp[2] = 2
        dp[0] = 0 + dp[1] = 2

        
        2710

        dp[4] = 1
        dp[3] = 0
        dp[2] = dp[3] + if allowed(dp[4]) = 1
        dp[1] = dp[2] + if(dp[3])x = 1
        dp[0] = dp[1] + (dp[2])

        '''

        dp = {len(s): 1}

        if s[-1] == '0':
            dp[len(s)-1] = 0
        else:
            dp[len(s)-1] = 1

        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]

        return dp[0]
                    
                
            
            


            
           
        