# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        '''
         
         Root L R
         preorder = [1,2,4,5,3,6,7]
         
         
         
         L R Root
         postorder = [4,5,2,6,7,3,1]
                      0 1 2 3 4 5 6
        (0-6) 
         1
   (0-5)        (0 - 5)
    2              3      
      (0-1)    (0 -2)
4      5        6                

         
        
        '''
        def findIndex(arr, l, r, target):
            for i in range(l, r + 1):
                if arr[i] == target:
                    return i
            
            
            return -1
        
        
        def constructTree(l, r):
            if l > r or len(preorder) == 0:
                return None
            
            index = findIndex(postorder, l, r, preorder[0])
            
            if index == -1:
                return None
            
            node = TreeNode(preorder.popleft())
            node.left = constructTree(l, index - 1)
            node.right = constructTree(l, index - 1)
            
            return node
    
        
        preorder = deque(preorder)
        l = 0
        r = len(preorder) - 1
        
        return constructTree(l, r)
        
