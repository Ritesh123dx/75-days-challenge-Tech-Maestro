class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        ans = [-1]*n
        
        for i in range(n - 1, -1, -1):
            
            while len(stack) > 0 and nums[i] >= stack[-1]:
                stack.pop()
                
            if len(stack):
                ans[i] = stack[-1]
            
            
            stack.append(nums[i])
            
        
        for i in range(n - 1, -1, -1):
            
            while len(stack) > 0 and nums[i] >= stack[-1]:
                stack.pop()
                
            if len(stack):
                ans[i] = stack[-1]
            
            
            stack.append(nums[i])
        
        
        return ans
        
