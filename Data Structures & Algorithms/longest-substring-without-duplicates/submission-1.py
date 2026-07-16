class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # keep moving r and adding to seen
        # at each step calculate best
        # if we land on a letter in seen:
            # while r is in seen, move l and remove l item from seen 
        # return best

        if len(s) == 1:
            return 1
        if len(s) == 0: 
            return 0

        r = 0
        l = 0

        best = 1

        seen = set()

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                best = max(best, r-l+1)
                r+=1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                best = max(best, r-l+1)

        return best

