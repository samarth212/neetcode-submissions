class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        adj = defaultdict(list)
        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)

        seen = set()
        def dfs(node, parent):

            seen.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                if n in seen: return False
                if not dfs(n, node): return False


            return True

        for node in range(n):
            if node not in seen:
                if not dfs(node, -1):
                    return False

        return True

                    
        

            

        