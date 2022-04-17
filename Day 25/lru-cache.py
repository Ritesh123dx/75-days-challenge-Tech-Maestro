class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.front = Node(-1, -1)
        self.rear = Node(-1, -1)
        
        self.front.next = self.rear
        self.rear.prev = self.front
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.detachPointers(node)
        self.moveFront(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.detachPointers(node)
            self.moveFront(node)
        
        else:
            
            newNode = Node(key, value)
            self.hashmap[key] = newNode
            self.moveFront(newNode)
            
            self.size += 1
            
            if self.size > self.capacity:
                self.evict()
                self.size -= 1
    
    
    
    #Custom-Made Functions By Me
    
    def detachPointers(self, node):
        next_node = node.next
        prev_node = node.prev
        
        node.next = None
        node.prev = None
        
        next_node.prev = prev_node
        prev_node.next = next_node
    
    
    
    def moveFront(self, node):
        next_node = self.front.next
        node.prev = self.front
        node.next = next_node
        
        self.front.next = node
        next_node.prev = node
    
    
    def evict(self):
        last_node = self.rear.prev
        self.detachPointers(last_node)
        del self.hashmap[last_node.key]
        del last_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
