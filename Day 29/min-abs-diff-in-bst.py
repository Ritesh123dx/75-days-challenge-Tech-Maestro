# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 10**8
    prev = None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
            
            if self.prev != None:
                self.ans = min(self.ans, node.val - self.prev)
            
            self.prev = node.val
            
            dfs(node.right)
        
        
        
        dfs(root)
        
        return self.ans
                
