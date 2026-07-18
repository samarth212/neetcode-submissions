class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result, path = [], []

        # for each number, try all further numbers
        # need to keep track of the start idx of the path and how much more we need
        
        def dfs(start, remaining):

            if remaining == 0:
                result.append(path[:])
                return
            
            if start >= len(nums) or remaining < 0:
                return

            
            for i in range(start, len(nums)):

                # dont choose i

                # choose i if it doesnt surpass our goal
                if remaining - nums[i] >= 0:
                    path.append(nums[i])
                    dfs(i, remaining-nums[i])
                    path.pop()


        dfs(0, target)
        return result

                

            
