class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1

        def posPow(x, n):
            if n == 1: 
                return x
        
            return x*posPow(x, n-1)

       

        if n > 0:
            return posPow(x, n)
        else:
            return 1/posPow(x, abs(n))


        
        