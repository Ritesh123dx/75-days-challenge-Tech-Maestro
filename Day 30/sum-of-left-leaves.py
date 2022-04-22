# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(node):
            return node.left == None and node.right == None
        
        queue = deque()
        queue.append(root)
        total = 0
        
        while len(queue) > 0:
            queueLen = len(queue)
            
            for i in range(queueLen):
                
                node = queue.popleft()
                
                if node.left:
                    if isLeaf(node.left):
                        total += node.left.val
                    
                    else:
                        queue.append(node.left)
                
                
                if node.right:
                    queue.append(node.right)
            
            
        
        return total
    
    
      
