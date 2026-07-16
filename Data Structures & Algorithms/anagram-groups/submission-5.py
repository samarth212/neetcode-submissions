class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        for i in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            hashmap.append(key)

        return list(hashmap.values())

        

        

        