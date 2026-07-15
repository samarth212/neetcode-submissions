class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in s:
            if i in hashmap:
                stack.append(i)
            else:
                if not stack or i != hashmap[stack.pop()]:
                    return False
        
        if stack:
            return False

        return True

        