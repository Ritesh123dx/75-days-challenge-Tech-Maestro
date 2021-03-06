class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        INT_MAX = 10**8
        n = len(grid)
        m = len(grid[0])
        
        dp = [[INT_MAX for j in range(m+1)] for i in range(n+1)]
        
        dp[0][1] = 0
        dp[1][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j - 1])
                
        
        
        return dp[n][m]
