class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        
        while r < len(s):
            hashmap[s[r]] += 1
            
            while hashmap[s[r]] == 2:
                hashmap[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        
        
        return ans
