class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        def checkRows():
            for r in range(9):
                seen = set()
                for c in range(9):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])

            return True

        def checkCols():
            for c in range(9):
                seen = set()
                for r in range(9):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])

            return True

        def check3x3(r, c):
            seen = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
            
            return True

        if not checkRows() or not checkCols():
            return False

        

        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                print(r, c)
                if not check3x3(r, c):
                    return False
        
        return True
                



        

        