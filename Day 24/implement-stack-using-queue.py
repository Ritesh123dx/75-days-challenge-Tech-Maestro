class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        n = len(self.queue)
        last_element = -1
        
        for i in range(n):
            last_element = self.queue.popleft()
            
            if i < n - 1:
                self.queue.append(last_element)
        
        return last_element

    def top(self) -> int:
        n = len(self.queue)
        last_element = -1
        
        for i in range(n):
            last_element = self.queue.popleft()
            self.queue.append(last_element)
        
        
        return last_element
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
