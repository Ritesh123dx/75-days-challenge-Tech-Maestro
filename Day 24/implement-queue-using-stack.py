class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.        
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        
        last_element = self.stack2.pop()
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        
        
        return last_element
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        
        last_element = self.stack2[-1]
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        
        
        return last_element
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
