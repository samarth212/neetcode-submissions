class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.end = True 

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        if not curr.end:
            return False
        return True 
         
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True 
        
        