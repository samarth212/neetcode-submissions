class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        temp = []
        ans = 0
        for i in tokens:
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
                    if i == 0:
                        ans = 0
                    else: ans //= i
                temp = []
            else:
                temp.append(int(i))
        
        return ans
        
        
        