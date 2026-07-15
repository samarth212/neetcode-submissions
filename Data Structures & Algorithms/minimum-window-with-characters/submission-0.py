class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # X: 1
        # Y: 1
        # Z: 2

        # X: 1
        # Y: 1
        # Z: 2

        #   L     
        # OOZOAYXOZOZ
        #         R


        # keep moving R until the freqs. of the chars in s match t
        # while its valid, move L up
        # keep resLen and res, update res if len(sol) >= resLen
        # if it lands on a char in the map, --
        # continue moving R up until the freq match again

        if not t or not s:
            return ""
        res = [-1, -1]
        resLen = len(s) +1
        l = 0

        #build freq. of t and s
        t_freq = {}
        for i in t:
            t_freq[i] = 1 + t_freq.get(i, 0)

       
        need = len(t_freq)
        have = 0
        window = {}

        for r in range(len(s)):
            window[s[r]] =  1 + window.get(s[r], 0)
    
            if s[r] in t_freq and t_freq[s[r]] == window[s[r]]:
                have +=1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -=1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l+=1
            
        l, r = res
        return s[l:r+1] if resLen != len(s) +1 else ""
                




        