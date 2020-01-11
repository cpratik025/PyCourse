import unittest
from testing import main

class test_main(unittest.TestCase):
    def test_do(self):
        test_num =10
        result = main.do(test_num)
        self.assertEqual(result, 10)
    def test_do3(self):
        test_num =10
        result = main.do(test_num)
        self.assertEqual(result, 'abcdefg')
    def test_do1(self):
        test_num =10
        result = main.do(test_num)
        self.assertEqual(result, 15)
    def test_do2(self):
        test_num ='abcded'
        result = main.do(test_num)
        self.assertEqual(result, 15)

unittest.main()