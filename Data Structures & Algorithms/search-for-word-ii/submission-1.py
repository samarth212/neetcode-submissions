class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        '''

        run a dfs(r, c, i) -> i is the index of char of a specific word
            check for out of bounds; return False
            check if r, c is in seen: return False
            if we reach end of word, add to res, return true

            return up or down or right or left if matches next letter

        for every word, 
        for every starting letter in the grid, initiate dfs(r, c, 0)


        '''

        seen = set()
        res = []
        def dfs(r, c, i, w):
            if i == len(w):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r, c) in seen: return False
            if board[r][c] != w[i]: return False


            seen.add((r, c))
            up = dfs(r-1, c, i+1, w)
            down = dfs(r+1, c, i+1, w)
            right = dfs(r, c+1, i+1, w)
            left = dfs(r, c-1, i+1, w)
            seen.remove((r, c))
    

            return up or down or right or left

        for word in words:
            seen = set()
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == word[0]:
                        if dfs(r, c, 0, word):
                            res.append(word)


        return res
