# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node : TreeNode)->TreeNode:
            if node == None:
                return None
            
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            
            node.left = right_subtree
            node.right = left_subtree
            
            return node
        
        
        return dfs(root)