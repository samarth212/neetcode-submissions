class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()
        best = 1
        ans = 1

        for i in range(1, len(nums)):
          
            if nums[i] == nums[i-1] + 1:
                ans +=1
            elif nums[i] != nums[i-1]:
                ans = 1
            best = max(ans, best)

        return best




        