class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        
        for i, j in prerequisites:
            adj[i].append(j)


        res = []
        visited, visiting = set(), set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


