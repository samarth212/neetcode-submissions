"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # create copy nodes

        if not head:
            return None
        
        nodes = {}
        c = head
        while c:
            new = Node(c.val)
            nodes[c] = new
            c = c.next

        c1 = head
        while c1:
            nodes[c1].next = nodes.get(c1.next)
            nodes[c1].random = nodes.get(c1.random)
            c1 = c1.next
        
        return nodes[head]
        




        