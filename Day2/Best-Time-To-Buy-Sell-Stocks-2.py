class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        profit = 0
        
        for i in range(1, n):
            if prices[i - 1] > prices[i]:
                profit += prices[i - 1] - buy
                buy = prices[i]
            
            if i == n - 1:
                profit += prices[i] - buy
        
        
        return profit
   
