class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        best = ''
        
        for i in range(len(s)):

            right = i + 1
            left = i - 1

            if i == 0:
                if s[right] == s[i]:
                    if len(s[right] + s[i]) > len(best):
                        best = s[i] + s[right]
            elif i == len(s)-1:
                if s[left] == s[i]:
                    if len(s[i] + s[left]) > len(best):
                        best = s[left] + s[i]
            else:
                while left >= 0 and right < len(s):

                    if s[right] == s[left]:
                        if len(s[left] + s[i] + s[right]) > len(best):
                            best = s[left] + s[i] + s[right]
                        right +=1
                        left -=1
                    elif s[i] == s[right]:
                        if len(s[right] + s[i]) > len(best):
                            best = s[i] + s[right]
                        right += 1
                    elif s[i] == s[left]:
                        if len(s[i] + s[left]) > len(best):
                            best = s[left] + s[i]
                        left -=1
                    else:
                        break
                        

                    

        return best


