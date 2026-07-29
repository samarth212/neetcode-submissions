class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
        generate a options list
        seen, stack
        res, path

        dfs(i)
        - if i >= len, and lenpath = len
            if stack is empty then append path else return
        
        - for all the items, 
            - skip j if in seen
            - if nums[j] adds to stack or closes pending, 
                add to stack and path and j to seen
                - do dfs(i+1)
                - remove those from stack and seen

        dfs(0)
        if stack is empty, return res else return []

        '''

        nums = (['('] * n) + ([')'] * n)
        seen = set()
        stack = []
        res = set()
        path = ''

        def dfs(i):
            nonlocal path
            if i >= len(nums):
                if not stack and len(path) == len(nums):
                    res.add(path[:])
                return

            for j in range(len(nums)):
                if j in seen:
                    continue
                if nums[j] == '(':
                    stack.append('(')
                    path += '('
                    seen.add(j)
                    dfs(i+1)
                    stack.pop()
                    path = path[:-1]
                    seen.remove(j)
                elif nums[j] == ')' and stack and stack[-1] == '(':
                    stack.pop()
                    path += ')'
                    seen.add(j)
                    dfs(i+1)
                    stack.append('(')
                    path = path[:-1]
                    seen.remove(j)
                elif nums[j] == ')' and not stack:
                    continue
        
        dfs(0)
        return list(res) if not stack else []
                





























