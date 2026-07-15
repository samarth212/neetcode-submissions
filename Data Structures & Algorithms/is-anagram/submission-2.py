class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = [0] * 26
        countT = [0] * 26

        for i in range(len(s)):
            charS, charT = s[i], t[i]
            countS[ord(charS)-ord('a')] += 1
            countT[ord(charT)-ord('a')] += 1

        if countT == countS:
            return True

        return False


        