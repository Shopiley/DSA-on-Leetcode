# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS - a level order traversal is needed
    
        # init res
        # add root to queue
        # pop and check for children
        # add children if any 

        # take the size of queue 
        # pop till size is zero
        # push children to children_arr
        # push children_arr to queue
        # children_arr = 0 
        

        # temp = []
        # init queue with root
        
        # for i in len(range(queue)) 
        # popleft, append to temp
        # append temp to res
        # if left, append to queue
        # if right, append to queue
        
        
#         queue = deque([root])
#         ans = []
        
#         while queue:
#             temp = []
#             kidz = []
#             size = len(queue)
            
#             for i in range(size):
#                 currentNode = queue.popleft()
#                 temp.append(currentNode)
#                 if currentNode.left:
#                     queue.append(currentNode.left)

#                 if currentNode.right:
#                     queue.append(currentNode.right)
            
#             queue.append(kidz)
#             ans.append(temp)
        
#         return ans


        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            next_queue = []
            level = []
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            queue = next_queue
        
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        