class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # for each 1 we encouter, perform dfs on all neighboring 1s
            # at each step, look left right up and down for 1s
            # if they are not in seen, recurse dfs passing in their position

        # continoulsy update set seen with the positions of seen 1s
        # once the dfs ends, increment count of islands by 1 
        # go to the next one whos position is not in the set of seen
        # once we reach the end of the grid and have passed through all the seen 1s, 
        # return count of islands

        seen = set()
        count = 0

        def dfs(pos):
            if not pos:
                return
            row = pos[0]
            col = pos[1]
            
            # at each step, look left right up and down for 1s not in seen
            # if they are not in seen, recurse dfs passing in their position
            # add to seen

            seen.add((row, col))

            # dfs left
            if col > 0 and grid[row][col-1] == "1" and (row, col-1) not in seen:
                dfs((row, col-1))
            # dfs right
            if col < len(grid[0]) - 1 and grid[row][col+1] == "1" and (row, col+1) not in seen:
                dfs((row, col+1))
            # dfs up
            if row > 0 and grid[row-1][col] == "1" and (row-1, col) not in seen:
                dfs((row-1, col))
            # dfs down
            if row < len(grid) - 1 and grid[row+1][col] == "1" and (row+1, col) not in seen:
                dfs((row+1, col))

            return 


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs((row, col))
                    count += 1

        
  
            
        return count




