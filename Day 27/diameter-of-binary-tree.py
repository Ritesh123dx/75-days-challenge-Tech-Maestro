# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node : TreeNode)->tuple[int]:
            if node == None:
                return (0, 0)
            
            Left_len, Left_diameter = dfs(node.left)
            Right_len, Right_diameter = dfs(node.right)
            
            max_dia = max(Left_diameter, Right_diameter, Left_len + Right_len)
            max_len = 1 + max(Left_len, Right_len)
            
            return (max_len, max_dia)
        
        
        return dfs(root)[1]