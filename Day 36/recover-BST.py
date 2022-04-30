# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    first, second = None, None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if node == None:
                return
            
            dfs(node.left)
           
            if self.prev != None and self.prev.val > node.val:
                if self.first == None:
                    self.first = self.prev
                    self.second = node
                
                else:
                    self.second = node
            
            self.prev = node
            
            
            dfs(node.right)
        
        
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
        
        
