class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        ans = list(s)
        stack = []
        
        n = len(s)
        
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
                    
        
        while len(stack):
            index = stack.pop()
            ans[index] = ""
        
        
        return "".join(ans)
