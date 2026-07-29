class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        seen = set()

        def dfs(i, sol):
            if i >= len(nums):
                key = tuple(sorted(sol))
                if key not in seen:
                    res.append(list(key))
                    seen.add(key)
                return
            
            sol.append(nums[i])
            dfs(i+1, sol)
            sol.pop()

            dfs(i+1, sol)

        dfs(0, [])
        return res

        