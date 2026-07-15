class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sortS = tuple(sorted(s))
        mySet = set()
        mySet.add(sortS)

        sortT = tuple(sorted(t))
        if sortT in mySet:
            return True 
        else: return False

        