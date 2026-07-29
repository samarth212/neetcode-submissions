class Solution:
    def partition(self, s: str) -> List[List[str]]:

        '''

        at each index, consider it as the middle

        consider as odd
            set l = r = i
            if l = r, add it to path
            prevEnd = r
            dfs(prevEnd+1)
            remove from path

        consider as even
            set l = i, r = i+1
            if l = r, add it to path
            prevEnd = r
            dfs(prevEnd+1)
            remove from path


        '''
        
        res = []
        path = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return res





        

        