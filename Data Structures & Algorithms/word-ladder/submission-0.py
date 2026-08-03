class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = defaultdict(list)
        for word in wordList:
            for char in range(len(word)):
                key = word[:char] + '*' + word[char+1:]
                adj[key].append(word)

        #print(adj)

        q = deque([beginWord])
        seen = set([beginWord])
        count = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count

                for char in range(len(word)):
                    key = word[:char] + '*' + word[char+1:]
                    
                    for child in adj[key]:
                        if child not in seen: 
                            q.append(child)
                            seen.add(child)
            count+=1

        return 0

