# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ''
        q = deque([root])

        while q:
            node = q.popleft()
            if node is None:
                s += ' ,'
            else:
                s += f'{node.val},'
                q.append(node.left)
                q.append(node.right)

        return s

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # 1,2,3,  4,5,    

        if not data:
            return None

        vals = [x.strip() for x in data.split(",")]

        if not vals or vals[0] == "":
            return None


        def build(i):
            if i >= len(vals) or vals[i] == "":
                return None

            node = TreeNode(int(vals[i]))
            node.left = build(2 * i + 1)
            node.right = build(2 * i + 2)
            return node

        return build(0)

            

                

