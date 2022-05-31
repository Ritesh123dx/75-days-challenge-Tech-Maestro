class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        
        left = 0
        right = 0
        for i in range(n):
            dp[i][i] = 1
            
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                left = i
                right = i + 1
        
        l = 3
        
        while l <= n:
            i = 0
            j = l - 1
            
            while j < n:
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    left = i
                    right = j
                    
                
                i += 1
                j += 1
            
            l += 1
        
        
        return s[left : right + 1]
        
    
