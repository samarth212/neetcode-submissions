class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        idx = 0
        while idx < n-1:
            for i in range(idx, n-1):
                temp1 = matrix[i][n-1]
                matrix[i][n-1] = matrix[idx][i]

                temp2 = matrix[n-1][-(i+1)] 
                matrix[n-1][-(i+1)] = temp1

                temp1 = matrix[-(i+1)][idx] 
                matrix[-(i+1)][idx] = temp2

                matrix[idx][i] = temp1
            n -= 1
            idx +=1

        
            