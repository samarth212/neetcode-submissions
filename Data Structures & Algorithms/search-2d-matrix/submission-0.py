class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         
        lr, lc = 0, 0
        m = len(matrix)-1
        n =  len(matrix[0])-1
        rr, rc = m, n

        searchRow = -1

        # find row
        while lr <= rr:
            mr = (lr + rr) // 2
            if matrix[mr][0] <= target <= matrix[mr][n]:
                searchRow = mr
                break
            elif target > matrix[mr][n]:
                lr = mr + 1
            else:
                rr = mr - 1

        print(searchRow)
        if searchRow == -1:
            return False

        while lc <= rc:
            mc = (lc + rc )// 2
            if matrix[searchRow][mc] == target:
                return True
            elif target > matrix[searchRow][mc]:
                lc = mc + 1
            else:
                rc = mc - 1


        return False



            

        # lr = 1
        # lc = 2
        # rr = 2
        # rc = 2
            

