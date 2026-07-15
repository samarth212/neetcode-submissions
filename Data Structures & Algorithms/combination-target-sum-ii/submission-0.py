class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # 1, 2, 2, 4, 5, 6, 9
        # ^

        candidates.sort()

        res = []

        def dfs(i, sol, remaining):

            if remaining == 0:
                res.append(sol[:])
                return
            if remaining < 0 or i == len(candidates):
                return
            
            if candidates[i] <= remaining:
                sol.append(candidates[i])
                print(sol)
                dfs(i+1, sol, remaining - candidates[i])
                sol.pop()
            
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, sol, remaining)


        dfs(0, [], target)
        return res


    


        