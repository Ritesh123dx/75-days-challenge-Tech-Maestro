class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        height = verticalCuts[0]
        
        for i in range(1, len(verticalCuts)):
            height = max(height, verticalCuts[i] - verticalCuts[i - 1])
        
        
        width = horizontalCuts[0]
        
        for i in range(1, len(horizontalCuts)):
            width = max(width, horizontalCuts[i] - horizontalCuts[i - 1])
        
        
        mod = 10**9 + 7
        return (height*width)%mod
