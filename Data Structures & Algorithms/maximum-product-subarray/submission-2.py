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

        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]

        for i in nums[1:]:
            prevMax = maxProd
            prevMin = minProd

            maxProd = max(i, prevMax*i, prevMin*i)
            minProd = min(i, prevMax*i, prevMin*i)
                
            result = max(result, maxProd, minProd)

        return result
        





        


        