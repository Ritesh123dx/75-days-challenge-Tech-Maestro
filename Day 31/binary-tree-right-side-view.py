# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        queue = deque()
        queue.append(root)
        
        ans = []
        
        while len(queue) > 0:
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                
                if i == n - 1:
                    ans.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
        
        
        return ans
