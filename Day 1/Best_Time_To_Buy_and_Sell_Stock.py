class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxRight = 10**8
        
        ans = 0
        for val in prices:
            if maxRight > val:
                maxRight = val
            else:
                ans = max(ans, val - maxRight)
                
        
        return ans
