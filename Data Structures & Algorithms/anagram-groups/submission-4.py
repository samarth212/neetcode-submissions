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
            key = ''.join(sorted(i))
            if key not in hashmap:
                hashmap[key] = [i]
            else: 
                hashmap[key].append(i)

        return list(hashmap.values())

        

        

        