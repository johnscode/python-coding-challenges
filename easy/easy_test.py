import unittest

import easy


class MyTestFactorial(unittest.TestCase):
    def test_factorial_ints(self):
        self.assertEqual(1, easy.factorial(1), msg="expected 1")
        self.assertEqual(2, easy.factorial(2), msg="expected 2")
        self.assertEqual(6, easy.factorial(3), msg="expected 6")

    def test_factorial_negative(self):
        with self.assertRaises(ValueError,msg="expected value error for negative number"):
            easy.factorial(-4)

    def test_factorial_non_int(self):
        with self.assertRaises(TypeError, msg="expected type error for non-int"):
            easy.factorial(3.5)


class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual([1,1,2],easy.fibonacci(2),msg="expected 1,1,2")
        self.assertEqual([1,1,2,3],easy.fibonacci(3),msg="expected 1,1,2,3")
        self.assertEqual([1,1,2,3,5,8],easy.fibonacci(5),msg="expected 1,1,2,3,5,8")

    def test_fib_non_int(self):
        with self.assertRaises(TypeError, msg="expected type error for non-int"):
            easy.fibonacci(15.3)

    def test_fib_one_or_neg(self):
        with self.assertRaises(ValueError, msg="expected value error for n<2"):
            easy.fibonacci(1)

class TestPalindromeCheck(unittest.TestCase):
    def test_palindrome_check(self):
        self.assertEqual(easy.palindrome_check('abba'), True, 'expected true')
        self.assertEqual(easy.palindrome_check('aba'), True, 'expected true')
        self.assertEqual(easy.palindrome_check('abb'), False, 'expected true')
        self.assertEqual(easy.palindrome_check('bb'), True, 'expected true')

if __name__ == '__main__':
    unittest.main()
