class Node():
    def __init__(self):
        self.children = {}
        self.end = False
        

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root

        for i, c in enumerate(word):
            if c != '.':
                if c not in curr.children:
                    return False
            else:
                for code in range(97, 123):
                    temp = chr(code) + word[i+1:]
                    if self.searchFromNode(temp, curr):
                        return True
            
            curr = curr.children[c]
        
        return curr.end
    
    def searchFromNode(self, word, node):
        curr = node

        for i, c in enumerate(word):
            if c != '.':
                if c not in curr.children:
                    return False
            else:
                for code in range(97, 123):
                    temp = chr(code) + word[i+1:]
                    if self.searchFromNode(temp, curr):
                        return True
            
            curr = curr.children[c]
        
        return curr.end

