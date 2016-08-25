from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = defaultdict(TrieNode)
        self.is_end_node = False

    def add(self, cur_index, end_index, string):
        character = string[cur_index]
        child = self.children[character]
        if cur_index == end_index:
            child.is_end_node = True
        return child

    def search(self, cur_index, string):
        character = string[cur_index]
        if character not in self.children:
            return None
        else:
            return self.children[character]


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        end_index = len(word) - 1
        for i in xrange(0, len(word)):
            node = node.add(i, end_index, word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in xrange(0, len(word)):
            node = node.search(i, word)
            if not node:
                return False
        return node.is_end_node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in xrange(0, len(prefix)):
            node = node.search(i, prefix)
            if not node:
                return False
        return True

if __name__ == '__main__':
    trie = Trie()
    trie.insert("hello")
    trie.insert("there")
    trie.insert("bar")
    trie.insert("a")
    assert not trie.search("alakazam")
    assert trie.startsWith("he")
    assert trie.startsWith("hello")
    assert trie.startsWith("h")
    assert trie.search("a")
    assert trie.startsWith("a")
    assert not trie.startsWith("q")
    assert not trie.search("q")
