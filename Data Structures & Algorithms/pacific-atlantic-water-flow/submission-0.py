class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()

        def dfs_pacific(row, col):
            if (row, col) not in pacific:
                pacific.add((row, col))

                # dfs left
                if col > 0 and heights[row][col-1] >= heights[row][col] and (row, col-1) not in pacific:
                    dfs_pacific(row, col-1)
                # dfs right
                if col < len(heights[0]) - 1 and heights[row][col+1] >= heights[row][col] and (row, col+1) not in pacific:
                    dfs_pacific(row, col+1)
                # dfs up
                if row > 0 and heights[row-1][col] >= heights[row][col] and (row-1, col) not in pacific:
                    dfs_pacific(row-1, col)
                # dfs down
                if row < len(heights) - 1 and heights[row+1][col] >= heights[row][col] and (row+1, col) not in pacific:
                    dfs_pacific(row+1, col)


        def dfs_atlantic(row, col):
            if (row, col) not in atlantic:
                atlantic.add((row, col))

                # dfs left
                if col > 0 and heights[row][col-1] >= heights[row][col] and (row, col-1) not in atlantic:
                    dfs_atlantic(row, col-1)
                # dfs right
                if col < len(heights[0]) - 1 and heights[row][col+1] >= heights[row][col] and (row, col+1) not in atlantic:
                    dfs_atlantic(row, col+1)
                # dfs up
                if row > 0 and heights[row-1][col] >= heights[row][col] and (row-1, col) not in atlantic:
                    dfs_atlantic(row-1, col)
                # dfs down
                if row < len(heights) - 1 and heights[row+1][col] >= heights[row][col] and (row+1, col) not in atlantic:
                    dfs_atlantic(row+1, col)
                
        
        for i in range(len(heights[0])):
            dfs_pacific(0, i)
            dfs_atlantic(len(heights)-1, i)
        for i in range(len(heights)):
            dfs_pacific(i, 0)
            dfs_atlantic(i, len(heights[0])-1)


        sol = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i, j) in atlantic and (i, j) in pacific:
                    sol.append([i, j])

        return sol

        