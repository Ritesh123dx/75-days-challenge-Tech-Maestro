class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def getMaxFreq(hashmap):
            maxFreq = 0
            for char in hashmap.keys():
                maxFreq = max(maxFreq, hashmap[char])
            
            return maxFreq
        
        
        hashmap = defaultdict(int)
        n = len(s)
        ans = 0
        i, j = 0, 0
        maxFreq = 0
        
        while j < n:
            char = s[j]
            hashmap[char] += 1
            
            maxFreq = max(maxFreq, hashmap[char])
            
            while maxFreq + k < (j - i + 1):
                hashmap[s[i]] -= 1
                maxFreq = getMaxFreq(hashmap)
                i += 1
            
            ans = max(ans, j - i + 1)
            j += 1
        
        
        return ans
