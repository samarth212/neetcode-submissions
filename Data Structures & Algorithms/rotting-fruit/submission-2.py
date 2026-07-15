class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # init queue
        # find a 2
        # start off q with r, c of that 2
        # for each r, c in the q, we change its neighs to 2
        #  -> lwhen we use a item we pop it from q
        # add its children to q
        # once q is empty (we break out of for loop), incremment mins
        # repeat until q is fully empty

        # loop through and run this check for all 2s
        # finally loop through and check if there are any 1s
        # return min or -1

        mins = 0
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        rows, cols = len(grid), len(grid[0])


        def bfs(q):
            nonlocal mins

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))

                if q:
                    mins += 1
                

                

        q = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))

        bfs(q)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return mins




                
            

            
