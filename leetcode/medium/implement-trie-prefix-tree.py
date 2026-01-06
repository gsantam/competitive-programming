class Trie:
    def __init__(self):
        self.children = {}
        self.terminal_words = 0

    def insert(self, word: str, pos = 0) -> None:
        if pos<len(word):
            letter = word[pos]
            if letter not in self.children:
                self.children[letter] = Trie()
            self.children[letter].insert(word,pos+1)
            if pos == len(word)-1:
                self.children[letter].terminal_words+=1

        

    def search(self, word: str, pos = 0) -> bool:
        if pos==len(word):
            if self.terminal_words>0:
                return True
            return False
        if pos<len(word):
            letter = word[pos]
            if letter in self.children:
                return self.children[letter].search(word,pos+1)
            else:
                return False

        

    def startsWith(self, prefix: str,pos = 0) -> bool:
        if pos==len(prefix):
            return True
        if pos<len(prefix):
            letter = prefix[pos]
            if letter in self.children:
                return self.children[letter].startsWith(prefix,pos+1)
            else:
                return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
