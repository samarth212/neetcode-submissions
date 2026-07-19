class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def dfs(r, c):

            if (r, c) in seen:
                return

            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return

            if grid[r][c] == "0":
                return

            seen.add((r, c))

            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    count +=1

        return count



            

            

            

            


            

        