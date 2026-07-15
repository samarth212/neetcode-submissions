class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]

            # skip nums[i]
            res = dfs(i + 1, prev)

            # take nums[i] if valid
            if prev == -1 or nums[i] > nums[prev]:
                res = max(res, 1 + dfs(i + 1, i))

            dp[(i, prev)] = res
            return res

        return dfs(0, -1)