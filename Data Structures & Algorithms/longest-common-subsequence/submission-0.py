class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        '''

        "samarth", "amamalyth"

        dfs(i, j): 
        base case: i or j reaches end -> return 1
        if i == j: 1 + dfs(i+1, j+1)
        else: 1 + max(dfs(i+1, j), dfs(j+1), i)

        '''

        dp = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in dp: return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
                return dp[(i, j)]

        return dfs(0, 0)
        