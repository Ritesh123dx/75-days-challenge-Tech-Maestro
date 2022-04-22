# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(node, minVal):
            if node == None:
                return 0
            
            good_node = 0
            if node.val >= minVal:
                good_node = 1
                minVal = node.val
                
            return good_node + dfs(node.left, minVal) + dfs(node.right, minVal)
        
        
        INT_MIN = -10**9
        return dfs(root, INT_MIN)
