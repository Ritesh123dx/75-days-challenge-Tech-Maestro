class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)
        isPalindrome = [[False for j in range(n)] for i in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True
        
        
        string_len = 3
        while string_len <= n:
            l = 0
            r = string_len - 1
            
            while r < n:
                if s[l] == s[r] and isPalindrome[l + 1][r - 1]:
                    isPalindrome[l][r] = True
                
                l += 1
                r += 1
            
            string_len += 1
        
        
        
        
        def partition(i, j):
            if i >= j or isPalindrome[i][j]:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            min_cuts = 10**9
            
            for k in range(i, j):
                if isPalindrome[i][k]:
                    cuts = 1 + partition(k + 1, j)
                    min_cuts = min(min_cuts, cuts)
            
            
            
            dp[i] = min_cuts
            return min_cuts
        
        
        dp = [-1 for i in range(n)]
        
        return partition(0, n - 1)
        
