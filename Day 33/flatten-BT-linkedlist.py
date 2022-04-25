# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    
    def dfs(self, node):
        if node == None:
            return
        
        self.dfs(node.right)
        self.dfs(node.left)
        
        if self.prev == None:
            self.prev = node
        else:
            node.right = self.prev
            node.left = None
            self.prev = node
            
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.dfs(root)
        
        return self.prev
        
    
                
