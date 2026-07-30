class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        '''

        [1,2,4,2,3,5,3,4]
        [1,2,2,3,3,4,4,5]

        1:0
        2:0
        3:0
        4:0
        5:0

        groups = 2






   





        '''

        if len(hand)%groupSize != 0:
            return False

        hand.sort()
        freq = defaultdict(int)
        for i in hand:
            freq[i] += 1

        for i in hand:
            if freq[i] == 0: continue
            for j in range(i, i+groupSize):
                if freq[j] == 0: 
                    return False
                else: freq[j] -=1

        return True




      

        









        