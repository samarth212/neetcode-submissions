class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [[grid[0][0], 0, 0]]
        seen = set([(0, 0)])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n-1 and c==n-1:
                return t

            for dr, dc in dirs:
                if (r+dr, c+dc) in seen: 
                    continue 
                if r+dr >= n or r+dr < 0 or c+dc >= n or c+dc < 0:
                    continue

                seen.add((r, c))
                heapq.heappush(heap, (max(t, grid[r+dr][c+dc]), r+dr, c+dc))


                






        