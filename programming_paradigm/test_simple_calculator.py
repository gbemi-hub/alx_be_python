import unittest
from simple_calculator.py import SimpleCalculator

class TestMathfunction(unittest.TestCase):
    def test_add(self):
       self.assertEqual(add(2,3),5)

    def test_subtract(self):
       self.assertEqual(add(3,2),1)

    def test_multiply(self):
       self.assertEqual(add(2,3),6)

    def test_divide(self):
       self.assertEqual(add(4,2),2)
    
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError):divide(5,0)

if __name__ == "__main__"