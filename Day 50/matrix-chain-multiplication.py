
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        
        def MCM(i, j):
            if i == j:
                return 0
                
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = 10**9 + 7
            for k in range(i, j):
                operations = MCM(i, k) + MCM(k + 1, j) + arr[i - 1]*arr[k]*arr[j]
                ans = min(ans, operations)
            
            
            dp[i][j] = ans
            return ans
            
        dp = [[-1 for j in range(N)] for i in range(N)]
        return MCM(1, N - 1)

