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


class TestStack(unittest.TestCase):
    def test_pushpop(self):
        stack = intermediate.Stack()
        stack.push(x = "yoyo")
        stack.push(5)
        self.assertEqual(5, stack.pop(),msg="expected 5")
        self.assertEqual("yoyo", stack.pop(),msg="expected yoyo")
        self.assertEqual(None, stack.pop(),msg="expected None")


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = intermediate.LinkedList()
        ll.append(5)
        ll.append(6)
        self.assertEqual([5,6], ll.as_list(),msg="expected 5,6")

    def test_reverse(self):
        ll = intermediate.LinkedList()
        ll.append(5)
        ll.append(6)
        ll.reverse()
        self.assertEqual([6,5], ll.as_list(),msg="expected 6,5")
        self.assertEqual(6, ll.head.data,msg="expected 6")


class TestListEvenSquares(unittest.TestCase):
    def test_list_even_squares(self):
        print(intermediate.list_even_squares(20))


class TestCSVProcess(unittest.TestCase):
    def test_process(self):
        self.assertEqual(36, intermediate.process_file('./sample.csv'),msg="expected 36")

    def test_process_pandas(self):
        self.assertEqual(36, intermediate.process_pandas('./sample.csv'),msg="expected 36")

    def test_write(self):
        intermediate.write_data('./output.csv')

class TestDecorator(unittest.TestCase):
    def test_greet(self):
        self.assertEqual('HELLO WORLD', intermediate.hello(), msg='expected uppercase')


if __name__ == '__main__':
    unittest.main()

