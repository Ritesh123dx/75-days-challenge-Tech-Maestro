class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         1  2  3  4
#         5  6  7  8
#         9  10 11 12
#         13 14 15 16
        
        
#         1  5  9  13
#         2  6  10 14
#         3  7  11 15
#         4  8  12 16
        
#         13 9  5 1
#         14 10 6 2
#         15 11 7 3
#         16 12 8 4
        
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        l = 0
        r = n-1
        
        while l < r:
            for i in range(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            
            l += 1
            r -= 1
        
        
        
        
