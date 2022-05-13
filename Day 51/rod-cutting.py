
# 2D dp
class Solution:
    def cutRod(self, price, n):
        #code here

        rod_length = n
        dp = [[0 for j in range(rod_length + 1)] for i in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, rod_length + 1):
                if j - i >= 0:
                    dp[i][j] = max(price[i - 1] + dp[i][j - i], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
            
        
        return dp[n][rod_length]


# 1D dp
class Solution:
    def cutRod(self, price, n):
        #code here

        rod_length = n
        dp = [0 for j in range(rod_length + 1)]
        
        for i in range(1, n + 1):
            prev = dp[:]
            
            for j in range(1, rod_length + 1):
                
                if j - i >= 0:
                    dp[j] = max(price[i - 1] + dp[j - i], prev[j])
                else:
                    dp[j] = prev[j]
            
        
        return dp[n]


