# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append((root, 0))
        maxWidth = 0
        
        while queue:
            n = len(queue)
            left = 0
            right = 0
            for i in range(n):
                node, dist = queue.popleft()
                
                if i == 0:
                    left = dist
                
                if i == n - 1:
                    right = dist
                    
                if node.left != None:
                    queue.append((node.left, 2*dist + 1))
                
                if node.right != None:
                    queue.append((node.right, 2*dist + 2))
            
            
            maxWidth = max(maxWidth, right - left + 1)
        
        
        return maxWidth
    
    
        
