class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        # create instruction stack
        stack = []
        temp = ''
        for i in tokens[::-1]:
            if i == "+" or i == "-" or i == "*" or i == "/":
                if temp:
                    stack.append(temp)
                temp = i
            else:
                stack.append(int(i))
        stack.append(temp)
        
        # compute value using stack
        temp = ''
        ans = 0
        for i in stack[::-1]:
            if i == "+" or i == "-" or i == "*" or i == "/":
                temp = i
            else:
                if temp == "+":
                    ans += i
                elif temp == "-":
                    ans -= i
                elif temp == "*":
                    ans *= i
                elif temp == "/":
                    ans //= i

        return ans


        
        
        