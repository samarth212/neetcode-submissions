class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        '''

        two pointers, i and j
        consider the max values. if all them are <= the target, keep this one
            in this case, set i to j, and j to j+1
            before that return true if matches target
        else, move i while valid, set j = i+1
        and look for the next j

        target = [10, 9, 9]
     i
    [15,9,8],[2,4,4],[2,6,1],[10,9,4],[10,4,1],[2,12,11],[1,4,2],[15,1,14],[6,2,9],[4,5,11]
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
                if ai > x or bi > y or ci > z:
                    while triplets[i][0] > x or triplets[i][1] > y or triplets[i][2] > z:
                        i += 1
                        if i >= len(triplets):
                            return False
                        j = i+1
                else:
                    j+=1
        
        return False




        