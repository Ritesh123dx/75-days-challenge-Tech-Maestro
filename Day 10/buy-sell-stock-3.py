class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        
        def fun(index, isBought, k):
            if index == len(prices) or k == 0:
                return 0
            
            
            if (index, isBought, k) in dp:
                return dp[(index, isBought, k)]
            
            op1, op2 = 0, 0
            
            if isBought:
                op1 = prices[index] + fun(index + 1, not isBought, k - 1)
            
            else:
                op1 = -prices[index] + fun(index + 1, not isBought, k)
            
            
            op2 = fun(index + 1, isBought, k)
            
            ans = max(op1, op2)
            dp[(index, isBought, k)] = ans
            return ans
        
        
        dp = {}
        return fun(0, False, k)
    

