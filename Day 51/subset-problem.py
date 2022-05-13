class Solution:
    def isSubsetSum (self, N, arr, target):
        # code here 
     
        
        dp = [[False for j in range(target + 1)] for i in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = True
        
        for i in range(1, N + 1):
            for j in range(1, target + 1):
                
                if j - arr[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                
                else:
                    dp[i][j] = dp[i - 1][j]
        
        
        
        
        return dp[N][target]
                        
