class Solution:
    def gameOfLife(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        0 -> dead
        1 -> alive
        2 -> dead to alive
        3 -> alive to dead
        
        """
        def isValid(new_row, new_col, n, m):
            if new_row < 0 or new_row == n or new_col == m or new_col < 0:
                return False
            else:
                return True
        
        
        def countLives(matrix, row, col):
            
            n, m = len(matrix), len(matrix[0])
            lives = 0
            delta = [0, 1, -1]
            for x in delta:
                for y in delta:
                    if x == 0 and y == 0:
                        continue
                    
                    new_row = row + x
                    new_col = col + y
                    
                    if isValid(new_row, new_col, n, m):
                        if matrix[new_row][new_col] == 1 or matrix[new_row][new_col] == 3:
                            lives += 1
            
            return lives
        
        
        n, m = len(matrix), len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                lives = countLives(matrix, i, j)
                
                if matrix[i][j] == 1:
                    if lives < 2:
                        matrix[i][j] = 3
                        
                    elif lives > 3:
                        matrix[i][j] = 3
                
                elif matrix[i][j] == 0:
                    if lives == 3:
                        matrix[i][j] = 2
        
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 2:
                    matrix[i][j] = 1
                elif matrix[i][j] == 3:
                    matrix[i][j] = 0
        
                    
            
                        
        
