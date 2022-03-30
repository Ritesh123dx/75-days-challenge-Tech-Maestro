class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        
        s = 0
        for i in range(k):
            s += cardPoints[i]
        
        ans = s
        
        r = n - 1
        l = k - 1
        
        while l >= 0:
            s -= cardPoints[l]
            s += cardPoints[r]
            
            ans = max(ans, s)
            
            r -= 1
            l -= 1
        
        return ans
        
