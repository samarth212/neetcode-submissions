# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                res.append("null")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # 1,2,3,  4,5,    

        if not data:
            return None

        q = deque([root])
        i = 1

        vals = data.split(",")
        if vals[0] == "null":
            return None

        while q and i < len(vals):
            node = q.popleft()

            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root

            

                

