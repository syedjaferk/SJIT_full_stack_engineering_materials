"""
Words:

    apple
    application
    apply
    app
    banana

Query:
    app

Answer:
    4

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.is_end = True # Last character Node.

    def count_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count

trie = Trie()
trie.insert("apple")
trie.insert("application")
trie.insert("apply")
trie.insert("app")
trie.insert("banana")

print(trie.count_prefix("appli"))
