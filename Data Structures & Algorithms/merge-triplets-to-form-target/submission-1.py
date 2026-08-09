class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        '''

        two pointers, i and j
        consider the max values. if all them are <= the target, keep this one
            in this case, set i to j, and j to j+1
            before that return true if matches target
        else, keep i and look for the next j

        target = [9, 18, 12]
                                                        i
        [1, 2, 3], [4, 9, 14], [5, 5, 10], [5, 5, 11], [9, 15, 11], [9, 18, 12], [9, 15, 11]
                                                                     j

        
        '''

        if len(triplets) == 1:
            if triplets[0] == target: return True
            else: return False

        x, y, z = target

        i, j = 0, 1

        while j < len(triplets):
            ai, bi, ci = triplets[i]
            aj, bj, cj = triplets[j]

            a, b, c = [max(ai, aj), max(bi, bj), max(ci, cj)]

            if a <= x and b <= y and c <= z:
                if [a, b, c] == [x, y, z]:
                    return True
                triplets[j] = [a, b, c]
                i = j
                j +=1
            else:
                j+=1
        
        return False




        