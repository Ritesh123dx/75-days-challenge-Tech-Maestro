# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def preorderTraversal(self, node):
        if node == None:
            return "N"
        
        return str(node.val) + "," + self.preorderTraversal(node.left) + "," + self.preorderTraversal(node.right)
    
    
        
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        
        encoded = self.preorderTraversal(root)
        
        return encoded
        
    
    def constructTree(self, queue):
        if len(queue) == 0 or queue[0] == "N":
            queue.popleft()
            return None
        
        node = TreeNode(int(queue.popleft()))
        node.left = self.constructTree(queue)
        node.right = self.constructTree(queue)
        
        return node
    
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        queue = deque()
        for d in data:
            queue.append(d)
        
        
        return self.constructTree(queue)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
