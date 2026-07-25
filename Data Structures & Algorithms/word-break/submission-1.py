class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        '''
        s = "neetcode", wordDict = ["neet","code"]

        s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

        s = "ins", wordDict = ["in", "s", "i"]

        at every step, we can break or continue
        - if we break, recurse with remaining string to try to break that
        - if we continue, take the next element

        dfs(start, end)
        - if end of s and start:end exists, return true else return false
        - if start:end in wordDict: return dfs(end+1, end+1) or dfs(start, end+1)
        - else, return dfs(start, end+1)

        '''

        wordSet = set(wordDict)

        dp = {}

        def dfs(start, end):
            if end == len(s)-1:
                if s[start:end+1] in wordSet:
                    return True
                else: return False

            if (start, end) in dp:
                return dp[(start, end)]
            
            if s[start:end+1] in wordSet:
                res = (dfs(end+1, end+1) or dfs(start, end+1))
                dp[(start, end)] = res
                return dp[(start, end)]
            else:
                res = dfs(start, end+1)
                dp[(start, end)] = res
                return dp[(start, end)]

        return dfs(0, 0)


        
        