# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # handle null root
        # check if current 3 nodes satisfy BST props
        # recurse left subtree
        # recurse right subtree

        if not root:
            return True

        if root.left and root.right:
            if root.left.val < root.val < root.right.val:
                # recurse
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False
        elif not root.left and root.right:
            if root.val < root.right.val:
                # recurse
                return self.isValidBST(root.right)
            else:
                return False
        elif root.left and not root.right:
            if root.left.val < root.val:
                # recurse
                return self.isValidBST(root.left)
            else:
                return False
        else:
            return True





        
        