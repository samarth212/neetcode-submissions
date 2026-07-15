# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        q = deque([root])
        level = 0
        ans = []
        while q:
            level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_nodes.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else: continue
            ans.append(level_nodes)

            #level +=1

        return ans
            


        