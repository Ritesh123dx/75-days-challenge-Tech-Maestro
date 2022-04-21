# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(node, currSum, targetSum):
            if node == None:
                return False
            
            if node.left == None and node.right == None:
                return currSum + node.val == targetSum
            
            return dfs(node.left, currSum + node.val, targetSum) or dfs(node.right, currSum + node.val, targetSum)
            
            
        

        return dfs(root, 0, targetSum)
            
