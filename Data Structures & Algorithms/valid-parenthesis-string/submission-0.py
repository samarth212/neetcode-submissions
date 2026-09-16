class Solution:
    def checkValidString(self, s: str) -> bool:

        # loop through string, add open parentesis to stack
            # if countof ( is not 0, skip (effectively treating one of the * as a "") and decrement
        # if we encounter a close parenthesis, pop the stack
        # if we encounter a * and we have items in the stack, treat as close, else open
        # count number of * used as ) and (
        # if stack is empty and we encounter a ):
            # if countof ) is not 0, skip (effectively treating one of the * as a "") and decrement
            # else, return false early
        # at the end, if stack is empty, return true.
        # if the stack is not empty, return false
        

        # ()**)

        stack = 0
        opened = 0
        closed = 0

        for c in s:
            if c == '(':
                if opened > 0:
                    opened -= 1
                else:
                    stack+=1
            elif c == ')':
                if not stack:
                    if closed > 0:
                        closed -= 1
                    else:
                        return False
                else:
                    stack-=1
            else:
                if stack:
                    stack-=1
                    closed += 1
                else:
                    stack+=1
                    opened += 1
        
        if not stack:
            return True
        else: return False
                    
            



        
