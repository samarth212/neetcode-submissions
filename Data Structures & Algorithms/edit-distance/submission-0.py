class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # iterate through word1
        # at each step, we have 3 choices 
        # take the min of those choices

        dp = {}


        def dfs(i, j):
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return len(word2) - j

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i+1, j+1)
            
            insert = dfs(i, j+1)
            delete = dfs(i+1, j)
            replace = dfs(i+1, j+1)
            dp[(i, j)] = 1 + min(insert, delete, replace)
            return dp[(i, j)]

        return dfs(0, 0)
            

            

                
            
            

        