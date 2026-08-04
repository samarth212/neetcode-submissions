class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        visited = set()
        visiting = set()
        res = []

        adj = defaultdict(list)
        for from_i, to_i in tickets:
            adj[from_i].append(to_i)
        
        for airport in adj:
            adj[airport].sort(reverse=True)

        def dfs(node):

            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
              

            res.append(node)
            

        dfs('JFK')
        return res[::-1]

        