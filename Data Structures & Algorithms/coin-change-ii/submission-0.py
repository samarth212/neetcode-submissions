class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        '''

        keep frequency count to track dups

        backtrack and treat freq as the path

        dfs(target)
        - base case: target = 0, increase total
        - target < 0, return 

        for i in coins, if the diff >= 0, run dfs on diff

        '''

        total = 0
        frequencies = set()
        freq = [0] * len(coins)

        def dfs(target): 
            nonlocal total

            if target == 0:
                total += 1
                frequencies.add(tuple(freq[:]))
                return
            elif target < 0: 
                return

            for i in range(len(coins)):
                if target - coins[i] >= 0:
                    freq[i] +=1
                    if tuple(freq) not in frequencies:
                        dfs(target-coins[i])
                    freq[i] -=1

        dfs(amount)
        return total

        

