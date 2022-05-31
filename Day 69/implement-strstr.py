class Solution:
    def strStr(self, s: str, needle: str) -> int:
        if needle == "":
            return 0
        
        j = 0
        n = len(s)
        for i in range(n):
            if s[i] == needle[j]:
                
                if n - i + 1 >= len(needle):
                    ans = i
                    while j < len(needle) and i + j < n and s[i+j] == needle[j]:
                        j += 1
                    
                    if j == len(needle):
                        return ans
                    j = 0
                    
                else:
                    break
        
        return -1
