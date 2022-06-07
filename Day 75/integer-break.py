class Solution:
    def integerBreak(self, n: int) -> int:
        
        def f(n):
            if n == 1 or n == 2:
                return 1
            
            if n in dp:
                return dp[n]
            
            prod = 0
            
            for i in range(1, n):
                prod = max(prod, i*(n - i), f(i)*f(n - i), f(i)*(n - i))
            
            
            dp[n] = prod
            return prod
        
        
        dp = {}
        return f(n)