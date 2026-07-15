class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        best = 0
        

        def dfs(r, c):
            nonlocal best, seen, dirs
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
                return 0
            if (r, c) in seen:
                return 0
            if grid[r][c] == 1:
                seen.add((r, c))
                temp = 1
                for dr, dc in dirs:
                    temp += dfs(r+dr, c+dc)
                    best = max(temp, best)
                return temp
            

            return 0

        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r, c) not in seen and grid[r][c]==1:
                    dfs(r, c)
            

        return best

        


        