class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n==2:
            return n

        prev1, prev2 = 1, 2
        count = 0

        for i in range(2, n):
            count = prev1 + prev2
            prev1 = prev2
            prev2 = count

        return count
            



        
        