import unittest
from calculator import Calculator
#python -m unittest tests/tests_calculator.py
class Test_Calculator(unittest.TestCase):
    def test_soma1(self):
        self.assertEqual(3,Calculator.soma(1,2))
    def test_soma2(self):
        self.assertEqual(5, Calculator.soma(10,-5))
if __name__ == "__main__":
    unittest.main()