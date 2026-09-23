class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trusts = set()
        for node, nei in trust:
            trusts.add(node)

        for i in range(1, n+1):
            if i not in trusts:
                return i
        return -1
        