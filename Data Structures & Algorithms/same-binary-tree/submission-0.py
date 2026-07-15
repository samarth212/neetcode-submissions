# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        q1 = deque([(p, q)])
        
        while q1:
            pnode, qnode = q1.popleft()

            if not pnode and not qnode:
                continue
            elif not pnode or not qnode:
                return False
            else:
                if pnode.val != qnode.val:
                    return False
            
            q1.append((pnode.left, qnode.left))
            q1.append((pnode.right, qnode.right))

        return True
            

            
            
            

        