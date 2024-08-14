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


if __name__ == "__main__":
    unittest.main()
    
    