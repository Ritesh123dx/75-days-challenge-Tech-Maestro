# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def isSameTree(node1, node2):
            if node1 == None and node2 == None:
                return True
            
            if (node1 == None or node2 == None) or (node1.val != node2.val):
                return False
            
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)
        
        
        
        def dfs(node, subRoot):
            if node == None:
                return False
            
            if isSameTree(node, subRoot):
                return True
            
            if dfs(node.left, subRoot) or dfs(node.right, subRoot):
                return True
            else:
                return False
            
        
        return dfs(root, subRoot)
        
        
            