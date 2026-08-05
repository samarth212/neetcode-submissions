class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        '''

        build an adj which is distances of each point to every other point

        run union find, but pass in the total cost thus far
        every time we union, add up the totals + the distance between them 
        and make it the new total



        '''
        

        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))

        edges.sort()

        parent = list(range(n))
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]

            return True

        res = 0
        for distance, i, j in edges:
            if union(i, j):
                res += distance

        return res
                
                

                