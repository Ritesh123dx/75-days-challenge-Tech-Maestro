class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        
        self.nums.append(val)
        index = len(self.nums) - 1
        
        self.hashmap[val] = index
        
        return True
        

    def remove(self, val: int) -> bool:
        
        if val not in self.hashmap:
            return False
        
        n = len(self.nums)
        
        if val == self.nums[n - 1]:
            self.nums.pop()
            del self.hashmap[val]
        
        else:
            index = self.hashmap[val]
            
            last_num = self.nums[n - 1]
            last_num_index = n - 1
            
            self.hashmap[last_num] = index
            self.nums[index] = last_num
            
            self.nums.pop()
            del self.hashmap[val]
        
        
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
