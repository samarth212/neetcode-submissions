class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
            
        seen = set()
        seen.add(s[0])
        ans = 1
        left = 0
        right = 1

        while right < len(s):

            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                ans = max(ans, right - left)
            else:  
                seen.remove(s[left])
                left +=1

        return ans


            
            
        