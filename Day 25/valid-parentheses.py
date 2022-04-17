class Solution:
    def isValid(self, s: str) -> bool:
        
        def check(popped, char):
            if popped == '(':
                return char == ')'
            
            elif popped == '{':
                return char == '}'
            
            elif popped == '[':
                return char == ']'
        

        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False
                
                popped = stack.pop()
                if check(popped, char) == False:
                    return False
                
        
        return len(stack) == 0
