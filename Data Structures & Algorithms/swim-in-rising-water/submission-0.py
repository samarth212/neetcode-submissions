class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        '''

        run a bfs from 0, 0

        check if we can go up down right or left

        at each level, increment count and t

        base case: return count when we reach the bottom right

        '''


        t = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set([(0, 0)])
        q = deque([(0, 0)])

        def bfs(t):
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    if r == len(grid)-1 and c == len(grid[0])-1:
                        return True

                    for dr, dc in dirs:
                        if (r+dr, c+dc) in seen: 
                            continue 
                        if r+dr >= len(grid) or r+dr < 0 or c+dc >= len(grid[0]) or c+dc < 0:
                            continue
                        if grid[r][c] <= t and grid[r+dr][c+dc] <= t:
                            q.append((r+dr, c+dc))
                            seen.add((r+dr, c+dc))

            return False

            

        while t>=0:
            if bfs(t):
                return t
            seen = set([(0, 0)])
            q = deque([(0, 0)])
            t+=1

        return t





        