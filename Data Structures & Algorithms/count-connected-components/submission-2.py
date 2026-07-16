class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        numEdges = 0
        added = set()
        for i in range(n):
            #can we add edge? -> numEdges +=1
            # check if neighbor is already in adj to skip edge placemnt

            if adj[i]:
                for j in adj[i]:
                    if [j, i] not in edges: 
                        numEdges += 1

            
            print(numEdges)
        return n - numEdges
