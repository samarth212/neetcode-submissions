class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # the node should not be a key
        # the node should exist in all adjs

        degree = [[0, 0] for _ in range(n + 1)]
        for node, nei in trust:
            degree[node][1] +=1
            degree[nei][0] +=1


        for i in range(len(degree)):
            if degree[i][0] == n-1 and degree[i][1] == 0:
                return i

        return -1





        
        