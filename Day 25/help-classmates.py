class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        
        stack = []
        ans = [0]*n
        
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and arr[i] <= stack[-1]:
                stack.pop()
            
            if len(stack):
                ans[i] = stack[-1]

            else:
                ans[i] = -1
            
            stack.append(arr[i])
            
        
        return ans
