# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def getTrees(low, high):
            if low > high:
                return [None]
            
            if (low, high) in hashmap:
                return hashmap[(low, high)]
            
            trees = []
            for i in range(low, high + 1):
                
                left_subtrees = getTrees(low, i - 1)
                right_subtrees = getTrees(i + 1, high)
                
                for left_subtree in left_subtrees:
                    
                    for right_subtree in right_subtrees:
                        
                        root = TreeNode(i)
                        root.left = left_subtree
                        root.right = right_subtree
                        
                        trees.append(root)
               
            
            hashmap[(low, high)] = trees
            return trees
        
        
        hashmap = {}
        return getTrees(1, n)
    
    

