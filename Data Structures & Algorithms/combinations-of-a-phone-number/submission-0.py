class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        path = ''

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def dfs(i):
            nonlocal res, path

            if i == len(digits):
                if path:
                    res.append(path[:])
                return

            for letter in letters[digits[i]]:
                path += letter
                dfs(i+1)
                path = path[:-1]

        dfs(0)
        return res


            

