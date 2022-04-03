class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        isNotPresent = True
        if val in self.indices:
            isNotPresent = False
        
        self.nums.append(val)
        index = len(self.nums) - 1
        
        self.indices[val].add(index)
        
        return isNotPresent
    

    def remove(self, val: int) -> bool:
        isPresent = True
        if val not in self.indices:
            return False
        
        last_index = len(self.nums) - 1
        val_index = self.indices[val].pop()
        
        last_val = self.nums[last_index]
        self.nums[val_index] = last_val
        
        self.indices[last_val].add(val_index)
        self.indices[last_val].remove(last_index)
        
        self.nums.pop()
        
        if len(self.indices[val]) == 0:
            self.indices.pop(val)
        
        return isPresent
        
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
