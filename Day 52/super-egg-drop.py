class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
    
       
        def eggBreak(eggs, floors, dp):
            if eggs == 0 or floors == 0:
                return 0
            if eggs == 1:
                return floors
            
            if dp[eggs][floors] != -1:
                return dp[eggs][floors]
            
            min_attempts = INT_MAX
            #We follow min(max) strategy to compute the answer.
            for f in range(1, floors + 1):
                curr_attempts = 1 + max(eggBreak(eggs - 1, floors - f, dp), eggBreak(eggs, f - 1, dp))
                
                min_attempts = min(min_attempts, curr_attempts)
            
            
            dp[eggs][floors] = min_attempts
            return min_attempts
        
        
        INT_MAX = 10**9
        dp = [[-1 for j in range(n + 1)] for i in range(k + 1)]
        return eggBreak(k, n, dp)
        
