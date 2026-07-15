class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums[::-1]
       
        output = [1]
    
        # insert pre int outputs 
        prev_product = 1
        for i in nums:
            if len(output) == len(nums):
                break
            output.append(prev_product * i)
            prev_product = prev_product * i
        
        # insert post into pres 
        prev_product = 1
        for i in reversed(range(len(nums))):
            output[i] *= prev_product
            prev_product = prev_product * nums[i]


        return output