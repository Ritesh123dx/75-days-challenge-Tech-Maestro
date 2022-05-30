class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(string, l, r):
            
            while l < r:
                if string[l] != string[r]:
                    return False
                
                l += 1
                r -= 1
                
            return True
        
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                if isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1):
                    return True
                else:
                    return False
            
            l += 1
            r -= 1
        
        
        return True
