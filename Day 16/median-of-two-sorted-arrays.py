class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        INT_MAX = 10**8
        INT_MIN = -10**8
        
        A, B = nums1, nums2
        n, m = len(A), len(B)
        
        if n > m:
            n, m = m, n
            A, B = B, A
        
        
        l, r = 0, n - 1
        total = n + m
        half = total//2
        
        while True:
            mid = (l + r)//2
            i = mid
            j = half - mid - 2
            
            Aleft = A[i] if i >= 0 else INT_MIN
            Aright = A[i + 1] if i + 1 < n else INT_MAX
            
            Bleft = B[j] if j >= 0 else INT_MIN
            Bright = B[j + 1] if j + 1 < m else INT_MAX
            
            if Aleft <= Bright and Bleft <= Aright:
                if total%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
            
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1
            
            
