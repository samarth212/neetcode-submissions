class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''

        at each position, paths = sum(right, down)
        base case: we reach the end, which means this is 1 possible path
        base case: we go out of bounds, which means this is not possible (0)


        '''

        dp = {}

        def dfs(r, c):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0

            if (r, c) in dp:
                return dp[(r,c)]

            dp[(r, c)] = dfs(r, c+1) + dfs(r+1, c)
            return dp[(r, c)]

        return dfs(0,0)



        