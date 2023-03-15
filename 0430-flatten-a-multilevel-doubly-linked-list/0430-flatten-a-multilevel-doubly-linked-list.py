"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
         1---2---3---4---5---6--NULL
                 |
                 7---8---9---10--NULL
                     |
                     11--12--NULL
        
        stack = [4, 7]

        """
        if not head:
            return head
        dummy = Node(0)
        curr, stack = dummy, [head]
        
        while stack:
            temp = stack.pop()
            
            if temp.next: stack.append(temp.next)
            if temp.child: stack.append(temp.child)
            curr.next = temp
            temp.prev = curr
            temp.child = None
            curr = temp   # moving current to temp
        dummy.next.prev = None  # making the first node .prev point to None instead of Node(0)
        return dummy.next
                
            
                
            
            