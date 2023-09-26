# Characters stored as next characters only.
# Start is an empty node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

# Trie Implementation with children characters
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                # insert character in children map as TrieNode
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True
    
    def search(self, word):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[c]
        # Prefixes do not count as full words in a trie unless explicitly inserted as so
        return current.endOfWord
    
    def startsWith(self, prefix):
        current = self.root
        for character in word:
            if character not in current.children:
                return False
            current = current.children[c]
        return True