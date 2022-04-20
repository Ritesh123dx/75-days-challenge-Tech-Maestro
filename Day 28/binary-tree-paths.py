# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def isLeaf(node):
            return node.left == None and node.right == None
        
        def fun(node, path_list):
            if node == None:
                return
            
            if isLeaf(node):
                path_list.append(str(node.val))
                
                path_string = "->".join(path_list)
                ans.append(path_string)
                
                path_list.pop()
                return
            
            path_list.append(str(node.val))
            fun(node.left, path_list)
            fun(node.right, path_list)
            
            path_list.pop()
            
        
        
        ans = []
        path_list = []
        fun(root, path_list)
        
        return ans
