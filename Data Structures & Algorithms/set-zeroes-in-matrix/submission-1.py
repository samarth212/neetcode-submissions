class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        def setZero(r, c):
            for col in range(cols):
                if col == c or matrix[r][col] == 0: 
                    continue
                matrix[r][col] = float('inf')
            for row in range(rows):
                if row == r or matrix[row][c] == 0: 
                    continue
                matrix[row][c] = float('inf')
    
        for r in range(rows):
            for c in range(cols): 
                if matrix[r][c] == 0: 
                    setZero(r, c)

        for r in range(rows):
            for c in range(cols): 
                if matrix[r][c] == float('inf'): 
                    matrix[r][c] = 0

        
        
            




        


        
        