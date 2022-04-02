class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def getArea(grid, row, col):
            
            queue = deque()
            queue.append((row, col))
            grid[row][col] = -1
            area = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while len(queue) > 0:
                
                r, c = queue.popleft()
                
                for x, y in directions:
                    new_r = r + x
                    new_c = c + y
                    
                    if new_r < 0 or new_r == n or new_c < 0 or new_c == m or grid[new_r][new_c] == -1 or grid[new_r][new_c] == 0:
                        continue
                    
                    grid[new_r][new_c] = -1
                    area += 1
                    
                    queue.append((new_r, new_c))
            
            
            return area
        
        
        n = len(grid)
        m = len(grid[0])
        area = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = max(area, getArea(grid, i, j))
        
        
        return area
