class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]
        
        prev_product = 1
        for i in nums:
            if len(nums) == len(res):
                break
            res.append(prev_product * i)
            prev_product = prev_product * i

        post_product = 1
        for i in reversed(range(len(nums))):
            res[i] *= post_product
            post_product *= nums[i]

        return res



            