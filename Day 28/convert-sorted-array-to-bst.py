# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        
        def fun(lb, ub, nums):
            if lb > ub:
                return None
            
            mid = (lb + ub)//2
            node = TreeNode(nums[mid])
            node.left = fun(lb, mid - 1, nums)
            node.right = fun(mid + 1, ub, nums)
            
            return node
        
        
        return fun(0, len(nums) - 1, nums)
