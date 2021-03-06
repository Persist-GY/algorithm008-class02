# https://leetcode-cn.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '#'


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in range(len(word)):
            node = node.setdefault(word[i], {})
        node.setdefault(self.end, True)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True