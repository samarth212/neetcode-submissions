class Solution:
    def reorganizeString(self, s: str) -> str:

        ''' 

        create a hashmap of each letter's frequency

        a:1
        x:1
        y:2

        max heap -> use the max letter
        if the max letter was just used, go to the next biggest
        if there are no other options ( its next item has no more), return ""
        store (-freq, key) in heap

        '''

        freq = defaultdict(int)
        res = []

        for c in s:
            freq[c] += 1
        
        heap = [(-f, key) for key, f in freq.items()]
        heapq.heapify(heap)
        prev = None


        while heap:

            f, key = heapq.heappop(heap)
       
        
            if key == prev:
                if not heap:
                    return ""
                else:
                    f2, key2 = heapq.heappop(heap)
                    res.append(key2)
                    prev = key2
                    f2+=1
                    if f2 <= -1:
                        heapq.heappush(heap, (f2, key2))

                    heapq.heappush(heap, (f, key))
            else:
                f+=1
                if f <= -1:
                    heapq.heappush(heap, (f, key))
                res.append(key)
                prev = key
        
        if len(res) != len(s):
            return ""

        return ''.join(res)
                




        

        