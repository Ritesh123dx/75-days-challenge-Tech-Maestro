class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)
        
        if n == 0:
            return []
        
        hashmap = {}
        for i in range(n):
            hashmap[s[i]] = i
        
        ans = []
        length = 0
        end = 0
        
        for i in range(n):
            char = s[i]
            end = max(end, hashmap[char])
            length += 1
            
            if i == end:
                ans.append(length)
                length = 0
        
        
        return ans

