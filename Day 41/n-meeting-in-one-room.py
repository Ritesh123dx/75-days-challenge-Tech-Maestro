class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        arr = []
        for i in range(n):
            arr.append((start[i], end[i]))
        
        arr.sort(key = lambda x : x[1])
        
        count = 0
        
        prev_end = -1
        for i in range(n):
            if prev_end < arr[i][0]:
                count += 1
                prev_end = arr[i][1]
        
        
        return count
