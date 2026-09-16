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
        low = 0
        high = 0

        for c in s:
            if c == '(':
                low +=1
                high +=1
            elif c == ')':
                low -= 1
                high -=1
            else:
                low -=1
                high +=1
        
            if high < 0:
                return False
            low = max(low, 0)

        if low == 0:
            return True
        
        return False
                    
            



        
