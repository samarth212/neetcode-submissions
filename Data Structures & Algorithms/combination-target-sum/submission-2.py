class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # result = []

        # if base case: result.append(copy of current sol)
        # return

        # for choice in choices

            # if violates contrains: continue

            # choose:
            # call backtrack
            # pop from sol/ undo choice

            # dont choose
            # call backtrack on next choice

        result = []

        def backtrack(index, remaining, sol):

            if remaining == 0:
                result.append(sol[:])
                return
            if remaining < 0 or index == len(nums):
                return

           
            if nums[index] <= remaining:
                sol.append(nums[index])
                backtrack(index, remaining - nums[index], sol)
                sol.pop()

            backtrack(index+1, remaining, sol)

        backtrack(0, target, [])

        return result



        