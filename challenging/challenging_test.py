import unittest
import challenging


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(challenging.check_for_anagram("listen", "silent"))
        self.assertFalse(challenging.check_for_anagram("hello", "world"))


class TestLRUCache(unittest.TestCase):
    def test_lru(self):
        cache = challenging.LRUCache(3)
        cache.__setitem__(1,'1')
        cache.__setitem__(2,'2')
        cache.__setitem__(3,'3')
        cache.__setitem__(4,'4')
        print(cache.items())
        cache.get(3)
        print(cache.items())


class TestTree(unittest.TestCase):

    tree = challenging.Tree()

    def setUp(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(8)

    def test_inorder(self):
        self.tree.inorder()

    def test_preorder(self):
        self.tree.preorder()

    def test_postorder(self):
        self.tree.postorder()

    def test_levelorder(self):
        self.tree.level_order()


class TestTrie(unittest.TestCase):
    def test_1(self):
        trie = challenging.Trie()
        trie.insert("previews")
        print(trie.search("preview"))

    def test_find_completions(self):
        trie = challenging.Trie()
        words_to_insert = ["apple", "app", "apricot", "banana", "bat", "bath", "cat"]
        for word in words_to_insert:
            trie.insert(word)
        root = trie.root
        complete_words = trie.find_completions(root)
        print(complete_words)

        ap_node = root.kids['a'].kids['p']
        ap_words = trie.find_completions(ap_node, "ap")
        print(ap_words)


if __name__ == "__main__":
    unittest.main()
    
    