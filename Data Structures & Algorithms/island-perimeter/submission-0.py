class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # run dfs, each call returns # of water edges 


        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c]==0:
                return 1
            if (r, c) in seen :
                return 0
            
            perimeter = 0
                
            seen.add((r, c))
            
            for dr, dc in dirs:
                perimeter += dfs(r+dr, c+dc)

            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

        
                
        