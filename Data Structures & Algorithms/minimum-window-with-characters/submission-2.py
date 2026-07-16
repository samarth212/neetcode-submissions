class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""
        res = [-1, -1]
        resLen = len(s) +1
        l = 0

        t_freq = defaultdict(int)
        for i in t:
            t_freq[i] += 1

        need = len(t_freq)
        have = 0

        window = defaultdict(int)

        for r in range(len(s)):
            window[s[r]]+=1

            if s[r] in t_freq and window[s[r]] == t_freq[s[r]]:
                have +=1
                
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -=1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -=1
                l +=1

        l, r = res
        return s[l:r+1] if resLen != len(s) +1 else ""

        
                    
                
                


        