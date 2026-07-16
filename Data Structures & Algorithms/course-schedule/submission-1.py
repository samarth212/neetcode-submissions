class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True
        if len(prerequisites) == 1:
            return True

        #   [ [0, 1], [1, 2], [5, 0], ]

        seen = set()

        # start at prerequisites[0][0]

        def dfs(i):

            if prerequisites[i][0] in seen:
                return False
            
            seen.add(prerequisites[i][0])

            # check if preq. is the first elem of some other item in array
            preq = prerequisites[i][1]

            for j in range(len(prerequisites)):
                if j == i:
                    continue
                if preq == prerequisites[j][0]:
                    # continue search
                    return dfs(j)

            return True

        
        return dfs(0)




        