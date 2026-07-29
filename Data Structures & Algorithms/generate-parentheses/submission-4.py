class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = set()
        path = ''
        opened = 0
        closed = 0

        def dfs():
            nonlocal path, opened, closed
            if len(path) == n*2:
                if opened == n and closed == n:
                    res.add(path[:])
                return

            if opened < n:
                path += '('
                opened +=1
                dfs()
                path = path[:-1]
                opened -=1
        

            if closed < opened:
                path += ')'
                closed +=1
                dfs()
                path = path[:-1]
                closed -=1
                

        dfs()
        return list(res)

            
            

        