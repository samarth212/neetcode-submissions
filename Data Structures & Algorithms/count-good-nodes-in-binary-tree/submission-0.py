# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs approach
        # keep track of res
        # within the dfs, keep track of local max, pass it in as param
        # if node.val > max, count++
        # dfs node.right, node.left, pass in max(max, node.val)
        # if node is empty -> return

        res = 0

        def dfs(node, curMax):
            nonlocal res

            if not node:
                return

            if node.val >= curMax:
                res +=1
                
            dfs(node.left, max(curMax, node.val))
            dfs(node.right, max(curMax, node.val))

        dfs(root, float("-inf"))

        return res
            


        