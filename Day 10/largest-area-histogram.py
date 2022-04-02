class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        n = 6
        [2, 1, 5, 6, 2, 3]
         0  1  2  3  2  5
         
         0  5  3  3  5  5          
         
         width = rightBoundary[i] - leftBoundary[i] + 1
         area = height[i]*width
         
        '''
        n = len(heights)
        leftBoundary = [0]*n
        stack = []
        
        for i in range(n):
        
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if len(stack):
                leftBoundary[i] = stack[-1] + 1
            
            
            stack.append(i)
        
        
        stack = []
        rightBoundary = [n - 1]*n
        
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if len(stack):
                rightBoundary[i] = stack[-1] - 1
            
            
            stack.append(i)
        
        
        
        area = 0
        for i in range(n):
            height = heights[i]
            width = rightBoundary[i] - leftBoundary[i] + 1
            
            area = max(area, height*width)
        
        
        return area
            
