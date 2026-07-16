class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in tokens:     
            if i == "+":
                ans = stack.pop() if stack else 0
                while stack:
                    ans += stack.pop()
                stack = [ans]
            elif i == "-":
                ans = stack.pop() if stack else 0
                while stack:
                    ans = stack.pop() - ans
                stack = [ans]
            elif i == "*":
                ans = stack.pop() if stack else 0
                while stack:
                    ans *= stack.pop()
                stack = [ans]
            elif i == "/":
                ans = stack.pop() if stack else 0
                while stack:
                    ans = stack.pop() // ans
                stack = [ans]
            else:
                stack.append(int(i))
            print(stack, ans)
        return ans

        


        
        
        