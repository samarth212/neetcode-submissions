class Solution:
    def numDecodings(self, s: str) -> int:

        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == '0':
                return 0
            if (s[i] == '2' and i < len(s)-1 and int(s[i+1]) > 6) or int(s[i])>2:
                return dfs(i+1)
            return dfs(i+1) + dfs(i+2)
            
        return dfs(0)
          
            
    


        