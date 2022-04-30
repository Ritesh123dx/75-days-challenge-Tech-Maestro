# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []
        stack = []
        temp = root
        if root == None:
            return None
        
        while True:
            while temp != None:
                stack.append(temp)
                temp = temp.left
            
            if len(stack):
                temp = stack.pop()
                inorder.append(temp.val)
                temp = temp.right
            else:
                break
        
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i+1]:
                return False
        
        return True
