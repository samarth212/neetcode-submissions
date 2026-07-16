class Solution:
    def rob(self, nums: List[int]) -> int:


        def robFirst():
            rob1, rob2 = 0, 0
            for n in range(len(nums)-1):

                temp = max(rob1 + nums[n], rob2)
            
                rob1 = rob2
                rob2 = temp

            return rob2

        def robLast():
            rob1, rob2 = 0, 0
            for n in range(1, len(nums)):

                temp = max(rob1 + nums[n], rob2)
            
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(robFirst(), robLast())
            
            
        