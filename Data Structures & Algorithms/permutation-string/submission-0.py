class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = {}
        for char in s1:
            freq[char] = 1 + freq.get(char, 0)

        l = 0
        r = len(s1) - 1

        temp_freq = {}
        for char in s2[l:r+1]:
            temp_freq[char] = 1 + temp_freq.get(char, 0)

        while r < len(s2):


            
            if temp_freq == freq:
                return True
            
            if temp_freq[s2[l]] <= 1:
                del temp_freq[s2[l]]
            else: temp_freq[s2[l]] -= 1
            l += 1
            r +=1
            if r < len(s2):
                temp_freq[s2[r]] = 1 + temp_freq.get(s2[r], 0)

   
            
            
        return False

                





        