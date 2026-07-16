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

        vals = data.split(',')

        def build(i):
            if i >= len(vals) or vals[i] == "null":
                return None

            node = TreeNode(int(vals[i]))
            node.left = build(2 * i + 1)
            node.right = build(2 * i + 2)
            return node

        return build(0)

            

                

