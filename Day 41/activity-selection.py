class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        
        arr = []
        for i in range(n):
            arr.append([start[i], end[i]])
        
        arr.sort(key = lambda x : x[1])
        
        count = 0
        prev_time = -1
        
        for i in range(n):
            start, end = arr[i]
            if prev_time < start:
                count += 1
                prev_time = end
        
        return count
