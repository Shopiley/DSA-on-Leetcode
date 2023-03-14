# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = [root]
        result = []
        count = 0
        
        while queue:
            level = []
            next_queue = []
            
            for node in queue:
                level.append(node.val)
                
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                                
                
            count += 1
            queue = next_queue
            

            if count%2 == 0:
                result.append(level[::-1])
                # print(queue)
            else:
                result.append(level)
                       
        return result
                