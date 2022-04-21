# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(node, p, q):
            if node == None or node == p or node == q:
                return node
            
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)
            
            if l != None and r != None:
                return node
            
            if l != None:
                return l
            else:
                return r
        
        
        
        return dfs(root, p, q)
