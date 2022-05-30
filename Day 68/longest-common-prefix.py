class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getPrefix(prefix, string):
            i = 0
            j = 0
            
            new_prefix = ""
            while i < len(prefix) and j < len(string):
                if prefix[i] == string[j]:
                    new_prefix += prefix[i]
                    i += 1
                    j += 1
                else:
                    break
            
            return new_prefix
                
                
        n = len(strs)
        
        if n == 0:
            return ""
        
        prefix = strs[0]
        for i in range(1, n):
            prefix = getPrefix(prefix, strs[i])
            
            
        return prefix
