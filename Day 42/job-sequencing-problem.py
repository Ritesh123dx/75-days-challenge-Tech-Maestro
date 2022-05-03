#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        
        
        arr = []
        maxDeadline = 0
        for i in range(n):
            job = Jobs[i]
            arr.append([job.profit, job.deadline])
            maxDeadline = max(maxDeadline, job.deadline)
            
        arr.sort(reverse = True)
        
        work = [-1]*(maxDeadline + 1)
        
        count = 0
        total = 0
        for i in range(len(arr)):
            profit, deadline = arr[i]
            
            j = deadline
            
            while j >= 1:
                if work[j] == -1:
                    work[j] = 1
                    count += 1
                    total += profit
                    break
                
                j -= 1
            
            if count == maxDeadline:
                break
        
        
        return [count, total]
