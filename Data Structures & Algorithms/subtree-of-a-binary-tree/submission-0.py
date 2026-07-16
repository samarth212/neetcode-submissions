# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot or not subRoot and root:
            return True
        elif not root and subRoot:
            return False
        stack = [root]
        substack = [subRoot]

        while stack and substack:
            node = stack.pop()
            subnode = substack[-1]

            if not node and not subnode:
                continue

            if node.val == subnode.val:
                if node.right and subnode.right and node.right.val == subnode.right.val and node.left and subnode.left and node.left.val == subnode.left.val:
                    subnode = substack.pop()
                    substack.append(subnode.right)
                    substack.append(subnode.left)
                elif not node.right and not subnode.right and not node.left and not subnode.left:
                    return True
         
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        if not substack:
            return True
        return False



        
        
        