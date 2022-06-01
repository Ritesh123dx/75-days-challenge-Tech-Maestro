class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def fun(l, r, k):
            if l > r:
                return 0
            
            hashmap = defaultdict(int)
            
            for i in range(l, r + 1):
                hashmap[s[i]] += 1
            
            ans = 0
            for i in range(l, r + 1):
                char = s[i]
                
                if hashmap[char] < k:
                    ans = max(fun(l, i - 1, k), fun(i + 1, r, k))
                    return ans
            
            
            return r - l + 1
        
        
        n = len(s)
        return fun(0, n - 1, k)
