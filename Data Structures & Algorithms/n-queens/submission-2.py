class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        '''
        loop through every row, and place a queen 
        
        dfs(r): 
        base case: if r > n
        for each c in r, if its == '.'), 
            place a Q (add to path)
            (every time we place a q, in our path grid, we mark
            all unavailable spots with an number (add a number))

            dfs(r+1)

            remove the Q and remove an x from all releavnt places

        if we dont add a Q in a row, return

        '''

        board = [['.'] * n for _ in range(n)]
        res = []

        def mark(r, c):

            for row in range(n):
                if row == r:
                    continue
                if board[row][c] == '.':
                    board[row][c] = '1'
                elif board[row][c] != 'Q':
                    val = int(board[row][c])
                    val +=1
                    board[row][c] = str(val)

            for col in range(n):
                if col == c: 
                    continue
                if board[r][col] == '.':
                    board[r][col] = '1'
                elif board[r][col] != 'Q':
                    val = int(board[r][col])
                    val +=1
                    board[r][col] = str(val)

            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == '.':
                        board[nr][nc] = '1'
                    elif board[nr][nc] != 'Q':
                        val = int(board[nr][nc])
                        val +=1
                        board[nr][nc] = str(val)
                    nr += dr
                    nc += dc

        def unmark(r, c):
            for row in range(n):
                if row == r:
                    continue
                if board[row][c] == '.':
                    continue
                elif board[row][c] != 'Q':
                    val = int(board[row][c])
                    val -=1
                    board[row][c] = str(val) if val > 0 else '.'

            for col in range(n):
                if col == c: 
                    continue
                if board[r][col] == '.':
                    continue
                elif board[r][col] != 'Q':
                    val = int(board[r][col])
                    val -=1
                    board[r][col] = str(val) if val > 0 else '.'

            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] != '.' and board[nr][nc] != 'Q':
                        val = int(board[nr][nc]) - 1
                        board[nr][nc] = str(val) if val > 0 else '.'

                    nr += dr
                    nc += dc

        def clean(board):
            for r in range(n):
                for c in range(n):
                    if board[r][c] != 'Q' and board[r][c] != '.':
                        board[r][c] = '.'
                board[r] = ''.join(board[r])

            return board

        def dfs(r, count):
            if r == n:
                if count == n:
                    cleaned = clean([row[:] for row in board])
                    res.append(cleaned)
                return

            for c in range(len(board[r])): 
                if board[r][c] == '.':
                    board[r][c] = 'Q'
                    count += 1
                    mark(r, c)
                    dfs(r+1, count)
                    board[r][c] = '.'
                    count -= 1
                    unmark(r, c)

        
        dfs(0, 0)
        return res
        

        