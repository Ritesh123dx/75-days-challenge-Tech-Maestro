class Node:
    def __init__(self, key : int, value : int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    
    def helperAddNode(self, root : 'BST', key, value):
        
        if root == None:
            return Node(key, value)
        
        if key == root.key:
            root.value = value
            return root
        
        
        if key > root.key:
            root.right = self.helperAddNode(root.right, key, value)
        else:
            root.left = self.helperAddNode(root.left, key, value)
        
        return root
    
    def addNode(self, key : int, value : int):
        
        self.root = self.helperAddNode(self.root, key, value)
        
    
    def helperFindKey(self, root : "BST", key):
        if root == None:
            return -1
        
        if root.key == key:
            return root.value
        
        if key > root.key:
            return self.helperFindKey(root.right, key)
        else:
            return self.helperFindKey(root.left, key)
    
    
    def findKey(self, key : int):
        
        return self.helperFindKey(self.root, key)
    
    
    def helperDeleteNode(self, root, key):
        if root == None:
            return
        
        if key > root.key:
            root.right = self.helperDeleteNode(root.right, key)
            return root
        
        elif key < root.key:
            root.left = self.helperDeleteNode(root.left, key)
            return root
        
        elif key == root.key:
            
            if root.left == None and root.right == None:
                return None
            
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            else:
                
                maxNode = self.findMaxNode(root.left)
                root.key = maxNode.key
                root.value = maxNode.value
                root.left = self.helperDeleteNode(root.left, maxNode.key)
                
                return root
    
    def deleteNode(self, key):
        
        self.root = self.helperDeleteNode(self.root, key)
            
                
    def findMaxNode(self, root):
        while root.right != None:
            root = root.right
        
        return root    
                
        
class MyHashMap:

    def __init__(self):
        self.M = 997  #size of hash_array
        self.arr = [None]*self.M  #initializing the array with None
        
        for i in range(997):
            self.arr[i] = BST()

    
    def put(self, key: int, value: int) -> None:
        index = key%self.M
        
        root = self.arr[index]
            
        root.addNode(key, value)
        
        self.arr[index] = root
   
        
            
    def get(self, key: int) -> int:
        index = key%self.M
        
        root = self.arr[index]
        
        return root.findKey(key)
        

    
    def remove(self, key: int) -> None:
        
        index = key%self.M 
        
        root = self.arr[index]
        
        root.deleteNode(key)
        
        self.arr[index] = root

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
