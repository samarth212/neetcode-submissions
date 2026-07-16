class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
          
        # 10 1 5 6 7 1

     

        l = 0
        r = 1
        best = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                best = max(best, profit)
            else:
                l += 1
            r += 1

        return best






        
