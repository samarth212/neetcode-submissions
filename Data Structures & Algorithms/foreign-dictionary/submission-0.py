class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # loop through and compare each word to the next
        # if they are different, the adj[first char] adds a neighbor of the secodn char

        # then run topological sort
        # return reversed order

        adj = {j:set() for i in words for j in i}


        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        visited, visiting = set(), set()
        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True

            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for i in adj:
            if not dfs(i):
                return ""

        res.reverse()
        res = ''.join(res)
        return res


                

        