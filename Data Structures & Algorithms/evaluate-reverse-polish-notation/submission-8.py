class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:     
            if i == "+":
                ans = stack.pop() + stack.pop()
                stack.append(ans)
            elif i == "-":
                ans = (-1*stack.pop()) + stack.pop()
                stack.append(ans)
            elif i == "*":
                ans = stack.pop() * stack.pop()
                stack.append(ans)
            elif i == "/":
                ans = stack.pop()
                if ans != 0:
                    ans = stack.pop() // ans
                stack.append(ans)
            else:
                stack.append(int(i))
        return ans

        


        
        
        