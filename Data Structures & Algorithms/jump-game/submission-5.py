class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def jump(i):
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            if nums[i] >= len(nums)-1:
                return True
            
            nextBest = -1
            nextIndex = i
            for j in range(1, nums[i]+1):
                if i+j >= len(nums):
                    return True
                if nums[i+j] >= nextBest:
                    nextIndex = i+j
                    nextBest = nums[i+j]

            
            return jump(nextIndex)

        return jump(0)
        