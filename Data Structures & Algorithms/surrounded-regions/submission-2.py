class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])

        unsurrounded = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # run only on borders
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O' or (r, c) in unsurrounded:
                return

            unsurrounded.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        # check borders for unsurrounded
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    dfs(i, j)

        # flip surrounded
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in unsurrounded:
                    board[i][j] = 'X'





            

        