import unittest
import beginner

class MyIsEven(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(True, beginner.is_even(0), "expected true")
        self.assertEqual( False, beginner.is_even(1),"expected true")
        self.assertEqual(False, beginner.is_even(2345), "expected true")
        self.assertEqual( True, beginner.is_even(100),"expected true")

class TestSumList(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(1, beginner.sum_list([1,0]), 'expected 1')
        self.assertEqual(5, beginner.sum_list([1,4]), 'expected 5')
        self.assertEqual(17, beginner.sum_list([3,7,2,5]), 'expected 17')

    def test_sum_list_with_strings(self):
        with self.assertRaises(TypeError, msg='expected type error'):
            beginner.sum_list(['a', 'b'])

class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual('abba', beginner.reverse_string('abba'), msg='expected same')
        self.assertEqual('ab', beginner.reverse_string('ba'), msg='expected ab')

    def test_reverse_with_int(self):
        with self.assertRaises(TypeError, msg= 'expected TypeError'):
            beginner.reverse_string(1)

    def test_reverse_with_int_array(self):
        with self.assertRaises(TypeError, msg= 'expected TypeError'):
            beginner.reverse_string([1,0])


if __name__ == '__main__':
    unittest.main()

