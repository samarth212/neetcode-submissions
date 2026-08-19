class Solution:
    def getSum(self, a: int, b: int) -> int:

   

        while b:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a



        