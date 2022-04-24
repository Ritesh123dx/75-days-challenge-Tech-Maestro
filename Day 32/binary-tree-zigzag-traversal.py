# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root == None:
            return []
        
        queue = deque()
        ans = []
        queue.append((root,0))
    
        
        while len(queue):
            t1, h = queue.popleft()
            
            if h == len(ans):
                ans.append([t1.val])
            else:
                ans[h].append(t1.val)
            
          

            if t1.left != None:
                queue.append((t1.left, h+1))
            if t1.right != None:
                queue.append((t1.right, h + 1))
       
        
        for i in range(len(ans)):
            if i%2 != 0:
                ans[i] = ans[i][::-1]


        return ans
        
        
