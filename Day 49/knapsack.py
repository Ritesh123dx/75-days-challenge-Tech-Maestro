class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp = [[0 for w in range(W + 1)] for i in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(W + 1):
            dp[0][i] = 0
        
        
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if j - wt[i - 1] >= 0:
                    dp[i][j] = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
    
        return dp[n][W]
    
