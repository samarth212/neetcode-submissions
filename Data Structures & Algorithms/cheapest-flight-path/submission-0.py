class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # run bfs for k+1 layers
        # calc the cheapest routes thus far, and check at each step if we have already reached dst
        # return cheapest at the end


 

        
        adj = defaultdict(list) 
        for node, nei, cost in flights: 
            adj[node].append([nei, cost])

        q = deque([(src, 0)])
        costs = {src: 0}

        for used in range(k+1):

            new = costs.copy()

            for _ in range(len(q)):
                node, cost = q.popleft()

                for nei, weight in adj[node]:
                    newCost = cost + weight
                    if newCost < new.get(nei, float('inf')):
                        new[nei] = newCost
                        q.append((nei, newCost))
            
            costs = new

    
        return costs.get(dst, -1)


                

        


        
        
        