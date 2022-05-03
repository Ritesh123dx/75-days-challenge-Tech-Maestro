class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,items,n):
        
        # code here
        
        arr = []
        
        for i in range(n):
            item = items[i]
            weight = item.weight
            value = item.value
            
            arr.append((value/weight, weight, value))
        
        
        arr.sort(reverse = True)
        ans = 0
        
        for i in range(n):
            ratio, weight, value = arr[i]
            
            if weight <= w:
                ans += value
                w = w - weight
            
            else:
                ans += ratio*w
                break
        
        return ans
        
