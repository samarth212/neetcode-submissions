class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == n-1:
            return True
        return False

        