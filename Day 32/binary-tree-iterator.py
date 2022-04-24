# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.stack = []
        self.node = root
        

    def next(self) -> int:
        while True:
            while self.node != None:
                self.stack.append(self.node)
                self.node = self.node.left
            
            if len(self.stack) > 0:
                self.node = self.stack.pop()
                val = self.node.val
                self.node = self.node.right
            
            break
        
        return val
        

    def hasNext(self) -> bool:
        return self.node != None or len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
