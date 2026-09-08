class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 0: return 0

        def posPow(x, n):
            if n == 0: return 1

            res = posPow(x, n // 2)

            if n % 2 == 0:
                return res * res
            else:
                return res * res * x

        res = posPow(x, abs(n))

        if n > 0:
            return res
        else:
            return 1 / res