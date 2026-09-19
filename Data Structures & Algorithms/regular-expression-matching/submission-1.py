class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # have 2 pointers i, j for each string, keep track of j+1 as well
        # if not wildcard and letters match, increment both
        # if not wildcard and j = . increment both
        # if wildcard then make decision tree
            # - basically for range of len(s) - i (remaining chars left), choose amount of letter and continue
            # if any of them return true, return true (it is possible to reach the end)
            # else return false ( no configuration of the wildcard will reach the end) 

        dp = {}

        def dfs(i, j):
            if i == len(s):
                while j+1 < len(p) and p[j+1] == '*':
                    j += 2
                return j == len(p)
            if j == len(p):
                return False
            if j == len(p)-1:
                if p[j] == '*':
                    pass
                else:
                    if i != len(s)-1 or s[i] != p[j]:
                        return False
                    return True
            
            if (i, j) in dp:
                return dp[(i, j)]
                
            if p[j+1] != '*':
                if s[i] == p[j] or p[j] == '.':
                    dp[(i, j)] = dfs(i+1, j+1)
                    return dp[(i, j)]
            else:
                for k in range(len(s)-i+1):
                    if dfs(i+k, j+2):
                        dp[(i, j)] = True
                        return dp[(i, j)]
                dp[(i, j)] = False
                return False


        return dfs(0, 0)
                

        