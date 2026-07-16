class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        best = 0
        

        def dfs(r, c, area):
            nonlocal best, seen, dirs
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return
            if (r, c) in seen:
                return
            if grid[r][c] == 1:
                seen.add((r, c))
                for dr, dc in dirs:
                    dfs(r+dr, c+dc, area+1)

            
            best = max(best, area)

        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in seen:
                    dfs(r, c, 0)
            

        return best


        


        