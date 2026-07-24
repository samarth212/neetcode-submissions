class Solution:
    def numDecodings(self, s: str) -> int:


        '''

        2710

        dp[4] = 1
        dp[3] = 0
        dp[2] = dp[3] + if allowed(dp[4]) = 1
        dp[1] = dp[2] + if(dp[3])x = 1
        dp[0] = dp[1] + (dp[2])

        n2 = 1
        n1 = 0
        temp = n1 + if(n2)
        n2 = n1
        n1 = temp

        '''

        n2 = 1

        if s[-1] == '0':
            n1 = 0
        else:
            n1 = 1

        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                temp = 0
            else:
                temp = n1
                if int(s[i:i+2]) <= 26:
                    temp += n2
            n2 = n1
            n1 = temp

        return n1
                    
                
            
            


            
           
        