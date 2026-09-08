class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        nums = {
            '0':0, 
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        
        def convert(num):
            place = 1
            res = 0
            for n in num[::-1]:
                res += place*(nums[n])
                place*=10
            return res

       

        return str(convert(num1)*convert(num2))



            
        