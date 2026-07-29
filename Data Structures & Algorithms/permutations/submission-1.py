class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        seen = set()
        def dfs(i):

            if i >= len(nums):
                if len(path) == len(nums):
                    res.append(path[:])
                return

            for j in range(len(nums)):
                if j in seen:
                    continue
                
                seen.add(j)
                path.append(nums[j])
                dfs(i+1)

                seen.remove(j)
                path.pop()


        dfs(0)
        return res



            



        