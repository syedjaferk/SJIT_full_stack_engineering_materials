class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()


    def insert(self, word):
        node = self.root

        for ch in word: # apple
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def print_trie(self):
        self._print(self.root, "")

    def _print(self, node, space):
        for ch, child in node.children.items():
            marker = " *" if child.is_end else "-"
            print(f"{space}{ch}{marker}")
            self._print(child, space + "   ")

    def _dfs(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)

        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, result)


    def suggestions(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        result = []
        self._dfs(node, prefix, result)
        return result



trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("application")
trie.insert("cat")
trie.insert("caterpillar")

trie.print_trie()

print(trie.suggestions('ab'))
