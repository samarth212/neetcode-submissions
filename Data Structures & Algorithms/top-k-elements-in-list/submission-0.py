from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # make a set out of nums

        # for each num in nums, check if in set
        # if it is, add it to hashmap and increment value by 1
        # {1: 1, 
        #  2: 2, 
        #  3: 3}
        
        # now loop through key, value bucket hdit

        numSet = set(nums)
        hashmap = defaultdict(int)

        for i in nums: 
            if i in numSet:
                hashmap[i] += 1

        maxFreq = max(hashmap.values())
        buckets = [[] for _ in range(maxFreq + 1)]

        for elem, freq in hashmap.items():
            buckets[freq].append(elem) 

        result = []

        for i in range(maxFreq, 0, -1):
            for j in buckets[i]:
                result.append(j)
            if len(result) == k:
                return result

        return result

