class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        temp = []
        ans = int(tokens[0])
        for i in tokens[1::]:
            if i == "+":
                ans += sum(temp)
                temp = []
            elif i == "-":
                for i in temp:
                    ans -= i
                temp = []
            elif i == "*":
                for i in temp:
                    ans *= i
                temp = []
            elif i == "/":
                for i in temp:
                    ans //= i
                temp = []
            else:
                temp.append(int(i))
        
        return ans
        
        
        