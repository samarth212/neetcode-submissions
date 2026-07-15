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

        count = 1

        def dfs(root):
            nonlocal count
            if root is None:
                return

            left = dfs(root.left)
            if left is not None:
                return left
            if count == k:
                return root.val
            count+=1
            
            return dfs(root.right)

        return dfs(root)
        
        
            




        