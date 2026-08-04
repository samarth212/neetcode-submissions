class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        visited = set()
        visiting = set()
        res = []

        adj = defaultdict(set)
        for from_i, to_i in tickets:
            adj[from_i].add(to_i)

        print(adj)

        def dfs(node):

            for nei in sorted(adj[node]):
                dfs(nei)
                

            res.append(node)
            

        dfs('JFK')
        return res[::-1]

        