class Solution:
    def rob(self, nums: List[int]) -> int:

        ans1 = 0
        ans2 = 0
        for i in range(0, len(nums), 2):
            ans1 += nums[i]
        for j in range(1, len(nums), 2):
            ans2 += nums[j]

        
        return max(ans1, ans2)
        