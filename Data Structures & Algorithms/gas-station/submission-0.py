class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        best = (float('-inf'), -1)

        for i in range(len(gas)):
            best = max((gas[i]/cost[i], i), best)

        
        return best[1]