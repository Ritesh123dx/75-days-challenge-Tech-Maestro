# User function Template for Python3

class Solution:
    def equalPartition(self, n, arr):
        # code here
        
        s = sum(arr)
        
        if s%2 != 0:
            return False
            
        target = s//2
        
        
        
        dp = [[False for j in range(target + 1)] for i in range(n + 1)]
        
        for i in range(target + 1):
            dp[0][i] = False
        
        for i in range(n + 1):
            dp[i][0] = True
        
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]]
                
                dp[i][j] = dp[i][j] or dp[i-1][j]
        
        
        return dp[n][target]
                
           
