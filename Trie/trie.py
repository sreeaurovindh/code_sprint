class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_word = False

    class Trie:
        def __init__(self):
            self.root = self.getNode()

        def getnode(self):
            return TrieNode()

        def char_to_index(self,ch):
            return ord(ch) - ord('a')

        def insert(self,key):
            crawl = self.root
            for item in key:
                index = self.char_to_index(item.lower())
                if not crawl.children[index]:
                    crawl.children[index] = self.getnode()
                crawl = crawl.children[index]
            crawl.is_end_word = True

        def search(self,key):
            crawl = self.root
            for item in key:
                index = self.char_to_index(item)
                if crawl[index] is None:
                    return False
                else:
                    crawl = crawl[index]
            return crawl.is_end_word and crawl is not None
