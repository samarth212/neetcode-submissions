class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        '''

        [2,4,-3,5]

        dfs(i)
            base case: i = len(nums)-1 -> return num

            loop through from i -> end
            max prod = max(max prod, max prod * j) 

            return max(max prod, dfs(i+1))

        '''

        dp = {}

        def dfs(i):

            if i == len(nums):
                return float('-inf')
            
            if i in dp:
                return dp[i]

            runningProd = 1
            best = float('-inf')

            for j in range(i, len(nums)):
                runningProd *= nums[j]
                best = max(runningProd, best)
            
            dp[i] = best

            return dp[i]

                
        return dfs(0)





        


        