class Node:
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal
        self.next = None
        self.prev = None

class MinStack:

    def __init__(self):
        self.size = 0
        self.head = Node(0, 0)
        

    def push(self, val: int) -> None:
        
        new_node = None
        if self.size == 0:
            new_node = Node(val, val)
        else:
            new_node = Node(val, min(val, self.head.minVal))
        
        self.head.next = new_node
        new_node.prev = self.head
        self.head = new_node
        self.size += 1
        

    def pop(self) -> None:
        
        prev_node = self.head.prev
        prev_node.next = None
        
        poppedNode = self.head
        
        self.head = prev_node
        self.size -= 1
        del poppedNode
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
