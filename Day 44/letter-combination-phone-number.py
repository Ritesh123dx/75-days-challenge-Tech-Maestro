class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        hashmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        
        def helper(idx, temp):
            if idx == len(digits):
                ans.append(temp)
                return
            
            for char in hashmap[digits[idx]]:
                helper(idx + 1, temp + char)
        
        ans = []
        helper(0, "")
        
        return ans