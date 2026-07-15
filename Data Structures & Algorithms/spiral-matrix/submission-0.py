class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        
        def spiral(grid):
            nonlocal res

            if len(grid) == 0:
                return

            if len(grid)==1 and len(grid[0])==1:
                res += grid[0]
                return


            rows = len(grid) 
            cols = len(grid[0])

            top = []
            right = []
            bottom = []
            left = []

            for i in range(rows):
                for j in range(cols):
                    if i == 0:
                        top.append(grid[i][j])
                    elif i == rows-1:
                        bottom.append(grid[i][j])
                    elif j == cols-1:
                        right.append(grid[i][j])
                    elif j == 0:
                        left.append(grid[i][j])

            res += top
            res += right
            bottom.reverse()
            res += bottom
            left.reverse()
            res += left

            inner = [row[1:cols-1] for row in grid[1:rows-1]]

            spiral(inner)

        spiral(matrix)
        return res

            
            # items in toprow
            # all items in rightmost col
            # items in bottom row (reverse)
            # items in left (reverse)