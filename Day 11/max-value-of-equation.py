class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
      
        
        queue = deque()
        ans = -10**9 + 7
        
        for xj, yj in points:
            
            while len(queue) > 0:
                xi, yi = queue[0]
                if xj - xi > k:
                    queue.popleft()
                else:
                    break
            
            
            if len(queue):
                xi, yi = queue[0]
                ans = max(ans, xj + yj + yi - xi)
            
            while len(queue) > 0:
                xi, yi = queue[-1]
                if yj - xj > yi - xi:
                    queue.pop()
                else:
                    break
            
            queue.append((xj, yj))
        
        
        
        return ans
                
                
            
            
