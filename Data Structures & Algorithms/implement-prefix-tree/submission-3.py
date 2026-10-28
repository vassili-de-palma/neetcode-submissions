
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        nd = self.root
        for ch in word:
            if ch not in nd.children:
                nd.children[ch] = TrieNode()
            nd = nd.children[ch]
        nd.isEnd = True
    
    def search(self, word: str) -> bool:
        nd = self.root
        for ch in word:
            if ch not in nd.children:
                return False
            nd = nd.children[ch]
        if nd.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        nd = self.root
        for ch in prefix:
            if ch not in nd.children:
                return False
            nd = nd.children[ch]
        return True 
        
        