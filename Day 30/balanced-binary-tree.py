# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):
            if node == None:
                return (0, True)
            
            left_height, isLeft_balanced = dfs(node.left)
            
            right_height, isRight_balanced = dfs(node.right)
            
            if (isLeft_balanced == False or isRight_balanced == False) or abs(left_height - right_height) > 1:
                return (0, False)
            
            return (1 + max(left_height, right_height), True)
            
            
        
        return dfs(root)[1]
