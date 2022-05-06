class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(count, temp, op, cl):
            if cl > op or op > n:
                return
            
            if count == 2*n:
                ans.append("".join(temp))
                return
            
            temp.append("(")
            helper(count + 1, temp, op + 1, cl)
            temp.pop()
            
            temp.append(")")
            helper(count + 1, temp, op, cl + 1)
            temp.pop()
        
        
        ans = []
        helper(0, [], 0, 0)
        
        return ans