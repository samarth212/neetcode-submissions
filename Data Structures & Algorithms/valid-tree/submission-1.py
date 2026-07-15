class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()

        def dfs(node, parent):

            seen.add(node)
            
            for child in adj[node]:
                if child == parent:
                    continue
                if child in seen:
                    return False
                if not dfs(child, node): return False
            
            return True

        
        for node in range(n):
            if node not in seen:
                if not dfs(node, -1):
                    return False

        return True


            
        

        