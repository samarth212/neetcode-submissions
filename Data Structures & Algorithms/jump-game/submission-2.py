class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def jump(i):
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
           
            return jump(i+nums[i])

        return jump(0)
        