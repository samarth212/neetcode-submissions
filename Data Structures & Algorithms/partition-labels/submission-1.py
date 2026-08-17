class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''

        get frequency count
        at each step keep track how many you have; decrement freq
        then, loop over set of current letters and check if all their freqs are
        0. if so, add len to the res and set len back to 0

        x: 0
        y: 0
        z: 2
        b: 3
        i: 1
        s: 1
        l: 1

        '''

        need = defaultdict(int)
        for i in s:
            need[i] +=1
        
        pending = set()
        count = 0
        res = []

        for i in s:
            pending.add(i)
            need[i] -=1
            count+=1
            if need[i] == 0:
                pending.remove(i)
            
            if not pending: 
                res.append(count)
                count = 0
          

        return res
