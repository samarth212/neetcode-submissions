class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        used = set()

        def dfs(r, c, k):

            if k == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r, c) in used or board[r][c] != word[k]:
                return False


            used.add((r, c))

            # up
            if r > 0:
                if dfs(r-1, c, k+1):             
                    used.remove((r, c))
                    return True
            # down
            if r < len(board) - 1:
                if dfs(r+1, c, k+1): 
                    used.remove((r, c))
                    return True
            # right
            if c < len(board[0]) - 1:
                if dfs(r, c+1, k+1): 
                    used.remove((r, c))
                    return True
            # left
            if c > 0:
                if dfs(r, c-1, k+1): 
                    used.remove((r, c))
                    return True

            used.remove((r, c))
            return False

            
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0): return True
        return False
        
                

        

    


        