class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        '''

        at every step, either choose a letter from s1 or s2

        dfs(i, j)
        - base case: if i reaches end, check if the remaining of j
            matches with s3
        - base case: vice versa
        
        choose i only if matches:
        add to path
        dfs(i+1, j)
        remove from path

        choose j only if matches: 
        add to path
        dfs(i, j+1)
        remove from path
        '''

        path = ''
        dp = {}

        def dfs(i, j): 
            nonlocal path

            if i == len(s1):
                return True if path + s2[j:] == s3 else False
            elif j == len(s2):
                return True if path + s1[i:] == s3 else False

            if (i, j) in dp: 
                return dp[(i, j)]

            path += s1[i]
            res = False
            if s3[:len(path)] == path:
                res = dfs(i+1, j)
            path = path[:-1]

            path += s2[j]
            if s3[:len(path)] == path:
                res = res or dfs(i, j+1)
            path = path[:-1]

            dp[(i, j)] = res
            return dp[(i, j)]

        return dfs(0, 0)










        