# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    idx = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        def dfs(node):
            if node == None:
                return None
            
            
            left = dfs(node.left)
            self.idx += 1
            
            
            if self.idx == k:
                return node.val
            
            right = dfs(node.right)
            
            if left != None:
                return left
            else:
                return right
            
            
        
        return dfs(root)
