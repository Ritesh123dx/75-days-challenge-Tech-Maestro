# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        ans = []
        queue = deque()
        queue.append(root)
        
        while len(queue):
            temp = []
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            ans.append(temp)
        
        
        return ans
