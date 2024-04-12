import unittest
from calculator import Calculator

class Test_Calculator(unittest.TestCase):
    def test_soma(self):
        valor1, valor2 = Calculator(1,2)
        self.assertEqual(3,Calculator.soma(valor1,valor2))
   
