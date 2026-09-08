class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry < 9:
                digits[i] += 1
                return digits
            else: 
                digits[i] = 0
                carry +=1
        
        if carry != 0:
            return [1] + digits
        else: return digits
        