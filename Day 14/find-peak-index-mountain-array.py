class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        
        while l <= r:
            mid = (l + r)//2
            
            if mid == 0:
                l = mid + 1
                continue
            
            
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid - 1] < arr[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
