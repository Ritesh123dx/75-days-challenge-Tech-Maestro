#User function Template for python3

class Solution:
    def findPath(self, matrix, n):
        # code here
        
        def dfs(row, col, n, matrix, path):
            if row < 0 or row == n or col < 0 or col == n or matrix[row][col] == 0 or matrix[row][col] == -1:
                return 
            
            if row == n - 1 and col == n - 1:
                ans.append("".join(path))
                return 
            
            matrix[row][col] = -1
            
            directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
            
            
            for x, y, d in directions:
                new_row = row + x
                new_col = col + y
                path.append(d)
                dfs(new_row, new_col, n, matrix, path)
                path.pop()
            
            matrix[row][col] = 1
            
            return
            
        
        ans = []
        path = []
        dfs(0, 0, n, matrix, path)
        
        return ans
        

