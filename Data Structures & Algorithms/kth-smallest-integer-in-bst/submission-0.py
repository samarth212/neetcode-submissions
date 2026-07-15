# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # in order traversal -> make an array
        # access arr[k-1]

        arr = []

        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        
        return arr[k-1]
            




        