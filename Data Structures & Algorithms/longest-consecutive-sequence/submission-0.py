class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums.sort()
        left = 0
        right = 1
        best = 0

        print(nums)
        while right < len(nums):
            print(right)
            while right < len(nums) and nums[right] == nums[right-1] + 1:
                right += 1
            print(right, 'aftr')
            l = (right - left) + 1
            if l > best:
                best = l
            left = right
            right = left + 1
         
        
        return best




        