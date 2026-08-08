class Node:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res = set()
        seen = set()

        def dfs(r, c, node, word):
            if r < 0 or r >= rows or c < 0 or c >= cols: return False
            if (r, c) in seen: return False
            if board[r][c] not in node.children: return False

            seen.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r+1, c, node, word)
                



            seen.remove((r, c))

            




        