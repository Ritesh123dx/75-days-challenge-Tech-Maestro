'''

Hashmap[freq] -> LRU

minFreq
currFreq


addELement to LRU -> add the node to the front
deleteElement from LRU -> delete the last element
getLastElement fron LRU

'''
class LRU:
    def __init__(self):
        self.size = 0
        self.front = Node(-1, -1)
        self.rear = Node(-1, -1)
        
        self.front.next = self.rear
        self.rear.prev = self.front
    
    def addNode(self, node):
        next_node = self.front.next
        
        self.front.next = node
        node.prev = self.front
        node.next = next_node
        next_node.prev = node
        
        self.size += 1
    
    
    def isEmpty(self):
        return self.size == 0
    
    def getLastNodeKey(self):
        return self.rear.prev.key
    
    def deleteLastNode(self):
        node = self.rear.prev
        
        prev_node = node.prev
        
        prev_node.next = self.rear
        self.rear.prev = prev_node
        
        node.next = None
        node.prev = None
        
        del node
        
        self.size -= 1
    
    
    def deleteNode(self, node):
        next_node = node.next
        prev_node = node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node
        
        node.next = None
        node.prev = None
        
        self.size -= 1

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

  


      
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        
        self.hashmap_nodes = {}
        self.LRU_map = defaultdict(lambda : LRU())
        

    def get(self, key: int) -> int:
        if key not in self.hashmap_nodes:
            return -1
        
        node = self.hashmap_nodes[key]
        self.updateNode(key)
        
        return node.value
    
    
    def updateNode(self, key):
        node = self.hashmap_nodes[key]
        freq = node.freq
        self.LRU_map[freq].deleteNode(node)
        
        if self.LRU_map[self.min_freq].isEmpty():
            self.min_freq += 1
        
        node.freq += 1
        
        self.LRU_map[freq + 1].addNode(node)
        
        
    
    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0:
            return
        
        if key in self.hashmap_nodes:
            node = self.hashmap_nodes[key]
            node.value = value
            self.updateNode(key)
        
        else:
            new_node = Node(key, value)
            self.hashmap_nodes[key] = new_node
            
            if self.size == self.capacity:
                self.evict()
                self.size -= 1
            
            self.min_freq = 1
            self.LRU_map[1].addNode(new_node)
            self.size += 1
    
    
    def evict(self):
        LRU = self.LRU_map[self.min_freq]
        evict_key = LRU.getLastNodeKey()
        
        del self.hashmap_nodes[evict_key]
        LRU.deleteLastNode()
        
        if LRU.isEmpty():
            self.min_freq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
