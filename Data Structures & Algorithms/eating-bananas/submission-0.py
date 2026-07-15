class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        values = range(max(piles)+1)

        l = 1
        r = max(piles)

        def calcHours(k):
            if k == 0: return float('inf')
            hours = 0
            for i in piles:
                hours += math.ceil(i/k)
            return hours


        res = r
        while l <= r:
            m = (l+r)//2
            if calcHours(m) > h:
                l = m + 1
            elif calcHours(m) <= h:
                res = m
                r = m - 1

       



        return res