# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root
        
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
                
            elif p.val > current.val and q.val > current.val:
                current = current.right    
            
            else:
                return current
                

#             # look for a node such that it's left and right are p and q
#             def DFS(root):

#                 if not root:
#                     return 0

#                 if (DFS(root.right) == p) and (DFS(root.left) == q):
#                     return root
                
            