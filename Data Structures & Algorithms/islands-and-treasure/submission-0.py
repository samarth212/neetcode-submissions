class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # loop through and perform following for all 0s

        # perform bfs
        # only move in that direction if that cell is not -1
        # if it is >0, update that cell by the level of bfs we are on
        # ONLY UPDATE IF level of bfs is < exisiting value at cell
        

        def bfs(sr, sc):
            q = deque([(sr, sc, 0)])
            visited = set([(sr, sc)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            level = 0

            while q:
            
                r, c, level = q.popleft()

                if grid[r][c] > 0 and level < grid[r][c]:
                    grid[r][c] = level

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] > 0:
                        visited.add((nr, nc))
                        q.append((nr, nc, level+1))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)


        


                
            


        