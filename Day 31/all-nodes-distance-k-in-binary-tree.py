# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        
        def dfs(node, parent, hashmap):
            if node == None:
                return
            
            hashmap[node] = parent
            
            dfs(node.left, node, hashmap)
            dfs(node.right, node, hashmap)
        
        
	   hashmap = {}
        dfs(root, None, hashmap)
        
        ans = []
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target)
        
        while len(queue) > 0 and k >= 0:
            queue_len = len(queue)
            
            for i in range(queue_len):
                node = queue.popleft()
                
                if k == 0:
                    ans.append(node.val)
                
                else:
                    parent = hashmap[node]
                    neighbours = [parent, node.left, node.right]
                    
                    for neighbour in neighbours:
                        if neighbour != None and neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)
            
            k -= 1
        
        
        return ans
            
