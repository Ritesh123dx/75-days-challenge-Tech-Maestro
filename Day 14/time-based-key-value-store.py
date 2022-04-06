class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.map[key].append([timestamp, value])
        
    
    def binarysearch(self, arr, timestamp):
        l = 0
        r = len(arr) - 1
        index = -1
        
        while l <= r:
            mid = (l + r)//2
            
            timestamp_prev = arr[mid][0]
            
            if timestamp_prev <= timestamp:
                index = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return index
        
        
    
    def get(self, key: str, timestamp: int) -> str:
        
        arr = self.map[key]
        
        index = self.binarysearch(arr, timestamp)
        
        if index == -1:
            return ""
        else:
            return arr[index][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
