class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        '''
        treat each cell as a the start
        
        dfs(r, c)
        - base case: if we hit edge or hit seen: update best len
        - for each direction:
            - if its increasing:
            - add to our seen
            - add 1 to pathLen
            - dfs(new dir)
            - remove from seen
            - decrement path

        '''

        rows, cols = len(matrix), len(matrix[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = [[-1]*cols for _ in range(rows)]

        def dfs(r, c):

            if dp[r][c] != -1:
                return dp[r][c]
    
            best = 1
            for dr, dc in dirs:
                if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols: continue
                if matrix[r+dr][c+dc] > matrix[r][c]:
                    best = max(1 + dfs(r+dr, c+dc), best)
            
            dp[r][c] = best
            
            return dp[r][c]

        res = 1
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))
        
        return res

      
     



            


        