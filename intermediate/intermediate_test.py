import unittest
import intermediate

class MyBinarySearch(unittest.TestCase):
    alist = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    def test_binary_search(self):
        self.assertEqual(0, intermediate.binary_search(2, self.alist), msg="expected 0")
        self.assertEqual(2, intermediate.binary_search(8, self.alist), msg="expected 2")
        self.assertEqual(9, intermediate.binary_search(91, self.alist), msg="expected 9")
        self.assertEqual(6, intermediate.binary_search(38, self.alist), msg="expected 6")
        self.assertEqual(5, intermediate.binary_search(23, self.alist), msg="expected 5")

    def test_odd_size_list(self):
        alist = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 99]
        self.assertEqual(10, intermediate.binary_search(99, alist), msg="expected 10")

    def test_not_found(self):
        self.assertEqual(-1, intermediate.binary_search(24, self.alist), msg="expected -1")

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual([1,2,3], intermediate.remove_duplicates([1,2,1,1,1,2,3,2,1,2]), msg="expected 1,2,3")

class TestMostFrequent(unittest.TestCase):
    def test_most_freq(self):
        self.assertEqual(1, intermediate.most_frequent([1,2,1,1,1,2,3,2,1,2]),msg="expected 1")


if __name__ == '__main__':
    unittest.main()

