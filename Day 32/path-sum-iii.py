# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        
        def dfs(node, currSum):
            if node == None:
                return 0
            
            currSum += node.val
            count = hashmap[currSum - targetSum]
            
            hashmap[currSum] += 1
            
            c1 = dfs(node.left, currSum)
            c2 = dfs(node.right, currSum)
            
            hashmap[currSum] -= 1
            currSum -= node.val
            
            return count + c1 + c2
        
        
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        
        return dfs(root, 0)
    
