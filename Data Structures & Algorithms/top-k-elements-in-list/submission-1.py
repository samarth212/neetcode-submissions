from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

       # make a bucket list
       # index is the freq (1->len(nums))
       # value is an array of nums with that freq
       # go backwards and append items into result
       # stop when len(result) = k and return 

       count = defaultdict(int)
       bucket = [[] for i in range(len(nums)+1)]

       for i in nums:
        count[i] += 1
       for num, freq in count.items(): 
        bucket[freq].append(num)

       result = []
       for i in range(len(bucket)-1, 0, -1):
        for j in bucket[i]:
            result.append(j)
        if len(result) == k:
            return result

       return result
        
       



    


