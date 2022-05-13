class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        '''
        dp[i] -> no of coins needed for ith denominations
        
        dp = 0  i  i  i  i  i  i  i  i  i   i   i         
             0  1  2  3  4  5  6  7  8  9  10  11
             
        
        dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
        '''
        INT_MAX = 10**9
        n = len(coins)
        dp = [INT_MAX]*(amount + 1)
        dp[0] = 0
        
        
        for i in range(1, amount + 1):
            for j in range(n):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
        
        return dp[i] if dp[i] != INT_MAX else -1
