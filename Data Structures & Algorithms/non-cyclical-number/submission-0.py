class Solution:
    def isHappy(self, n: int) -> bool:


        def calc(n):
            res = 0
            for i in str(n):
                res+= int(i)**2
            return res

        seen = set()
        while True:
            new = calc(n)
            if new == 1:
                return True
            if new in seen:
                return False
            seen.add(new)
            calc(new)
        


        return False