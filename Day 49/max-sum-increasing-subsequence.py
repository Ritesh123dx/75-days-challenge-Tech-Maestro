class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		
		mis = Arr[:]
		
		
        for i in range(n - 1):
            for j in range(i + 1, n):
                if Arr[j] > Arr[i]:
                    mis[j] = max(mis[j], mis[i] + Arr[j])

        return max(mis)
        
