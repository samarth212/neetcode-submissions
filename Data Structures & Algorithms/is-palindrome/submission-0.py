class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in s.lower():
            if i.isalnum():
                new += i

        return new == new[::-1]

        