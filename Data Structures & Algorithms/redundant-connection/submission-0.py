class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node) 

        seen = set()
        
        def dfs(node, parent): 
            seen.add(node)

            for nei in adj[node]:
                if nei == parent: 
                    continue

                if nei in seen:
                    return [True, [node, nei]]

                cycle, edge = dfs(nei, node)
                if cycle: 
                    return [True, edge]

            return [False, []]


        for node, _ in edges[::-1]:
            if node not in seen:
                cycle, edge = dfs(node, -1)
                if cycle: return sorted(edge)


        