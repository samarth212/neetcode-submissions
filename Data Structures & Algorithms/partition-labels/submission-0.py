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
        
        seen = set()
        count = 0
        res = []

        for i in s:
            seen.add(i)
            need[i] -=1
            count+=1
            skip = False
            for j in seen:
                if need[j] > 0:
                    skip = True
            if not skip:
                res.append(count)
                count = 0
                seen.clear()

        return res
