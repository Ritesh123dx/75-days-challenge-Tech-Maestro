class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        '''
        [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        
        [-2, 10] [9, 10]
        [-3, 15] [7, 15]
        [-5, 12] [12, 12]
        [-15,10] [20, 10]
        [-19, 8] [24, 8]
        
        
        
        [-2, 10] [-3, 15] [-5, 12] [7, 15] [9, 10] [12, 12] [-15, 10]
        
        [-19, 8] [20, 10] [24, 8]
        
        
        maxH = 8
        
        heap = [0 ]
        
        
        ans = [2, 10] [3, 15] [7, 12] [12, 0] [15, 10] [20, 8]
        '''
        
        def deleteFromHeap(heap, h):
            heap.remove(-h)
            heapq.heapify(heap)
        
        arr = []
        for l, r, h in buildings:
            arr.append([l, -h])
            arr.append([r, h])
        
        
        
        arr.sort()
        ans = []
        heap = [0]
        heapq.heapify(heap)
        max_height = 0
        
        for i in range(len(arr)):
            x, h = arr[i]
            
            if h < 0:
                if -h > max_height:
                    ans.append([x, -h])
                    max_height = -h
                    
                heapq.heappush(heap, h)
            
            else:
                deleteFromHeap(heap, h)
                
                if max_height > -heap[0]:
                    max_height = -heap[0]
                    ans.append([x, max_height])
        
        
        return ans
                    
