class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # save answer
        # loop through strs
        # start at the first, sort it and save as 
        # a key in a hashmap, with itself as a value

        # for each one after if it matches a key, add it 
        # to its values

        # finally return hashmaps' values

        hashmap = {}
        for i in strs:
            if sorted(i) not in hashmap.keys():
                hashmap[sorted(i)] = [i]
            else: 
                hashmap[sorted(i)].append(i)

        return hashmap.values()

        

        

        