class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(op, close, res, n):
            if op == close == n:
                ans.append("".join(res))
                return
            
            if op > n or close > op:
                return 
            
            res.append("(")
            generate(op + 1, close, res, n)
            res.pop()
            
            res.append(")")
            generate(op, close + 1, res, n)
            res.pop()
        
        
        ans = []
        generate(0, 0, [], n)
        
        return ans
