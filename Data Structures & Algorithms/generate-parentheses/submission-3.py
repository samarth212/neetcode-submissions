class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = set()
        path = ''
        stack = []

        def dfs():
            nonlocal path
            if len(path) == n*2:
                if not stack:
                    res.add(path[:])
                return

            path += '('
            stack.append('(')
            dfs()
            path = path[:-1]
            stack.pop()
     

            if stack:
                path += ')'
                stack.pop()
                dfs()
                path = path[:-1]
                stack.append('(')

        dfs()
        return list(res)

            
            

        