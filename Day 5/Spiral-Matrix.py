class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        ans = []
        r1, r2 = 0, n - 1
        c1, c2 = 0, m - 1
        
        while len(ans) < n*m:
            
            #go right
            for j in range(c1, c2 + 1):
                if len(ans) < n*m:
                    ans.append(matrix[r1][j])
                    
            
            r1 += 1
        
            #go down
            for i in range(r1, r2 + 1):
                if len(ans) < n*m:
                    ans.append(matrix[i][c2])
            
            c2 -= 1
            
            #go left
            for j in range(c2, c1 - 1, -1):
                if len(ans) < n*m:
                    ans.append(matrix[r2][j])
                    
            
            r2 -= 1
            
            #go up
            for i in range(r2, r1 - 1, -1):
                if len(ans) < n*m:
                    ans.append(matrix[i][c1])
                    
            
            c1 += 1
            
    
    
        return ans
