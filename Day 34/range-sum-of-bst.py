# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        def dfs(node, low, high):
            if node == None:
                return 0
            
            if node.val < low:
                return dfs(node.right, low, high)
            elif node.val > high:
                return dfs(node.left, low, high)
            else:
                return node.val + dfs(node.left, low, high) + dfs(node.right, low, high)
        
        
        
        return dfs(root, low, high)
