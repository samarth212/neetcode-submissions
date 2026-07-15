class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i, sol):
            if i >= len(nums):
                res.append(sol[:])
                return
            

            sol.append(nums[i])
            dfs(i+1, sol)
            sol.pop()

            dfs(i+1, sol)

        dfs(0, [])
        return res

          

        
        