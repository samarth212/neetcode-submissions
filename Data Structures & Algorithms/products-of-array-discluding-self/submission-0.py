class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # get the full product
        # loop through and for each item
        # divide product by itself and append

        product = 1
        result = []

        for i in nums:
            if i!=0:
                product *= i

        # -6
        for i in nums:
            if i == 0:
                result.append(product)
            elif 0 in nums:
                result.append(0)
            else:
                result.append(int(product/i))

        return result


        