class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        def helper(n, m):
            if n == 0:
                return m
            if m == 0:
                return n
            
            if dp[n][m] != -1:
                return dp[n][m]
            
            if word1[n - 1] == word2[m - 1]:
                return helper(n - 1, m - 1)
            
            val1 = 1 + helper(n - 1, m)  #del a word
            val2 = 1 + helper(n - 1, m - 1)  #replace a word
            val3 = 1 + helper(n, m - 1)   #insert a word
            
            temp = min(val1, val2, val3)
            dp[n][m] = temp
            
            return temp
            
        
        n = len(word1)
        m = len(word2)
        
        dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]
        
        return helper(n, m)
