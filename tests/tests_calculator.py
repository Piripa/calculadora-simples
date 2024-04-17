import unittest
from calculator import Calculator
# python -m unittest tests/tests_calculator.py


class Test_Calculator(unittest.TestCase):
    # Testes da soma
    def test_soma_valores_positivos(self):
        self.assertEqual(3, Calculator.soma(1, 2))

    def test_soma_valor_positivo_negativo(self):
        self.assertEqual(5, Calculator.soma(10, -5))

    def test_soma_valor_positivo_negativo(self):
        self.assertEqual(5, Calculator.soma(-5, 10))

    def test_soma_valores_negativos(self):
        self.assertEqual(-10, Calculator.soma(-5, -5))

    def test_soma_valor_positivo_nulo(self):
        self.assertEqual(5, Calculator.soma(5, 0))

    def test_soma_valores_negativo_nulo(self):
        self.assertEqual(-5, Calculator.soma(-5, 0))

    def test_divisao_valores_inteiros(self):
        self.assertEqual(1, Calculator.divisao(5, 5))

    def test_divisao_valores_negativos(self):
        self.assertEqual(1, Calculator.divisao(-5, -5))

    def test_divisao_valor_negativo_positivo(self):
        self.assertEqual(-1, Calculator.divisao(-5, 5))

    def test_divisao_valor_positivo_negativo(self):
        self.assertEqual(-1, Calculator.divisao(5, -5))

    def test_divisao_valores_fracionados(self):
        self.assertEqual(1, Calculator.divisao(2.5, 2.5))

    def test_divisao_valores_fracionados(self):
        self.assertEqual(1.25, Calculator.divisao(2.5, 1.5))

    def test_divisao_por_zero(self):
        self.assertEqual(0, Calculator.divisao(2, 0))

    def teste_divisao_zero_inteiro(self):
        self.assertEqual(0, Calculator.divisao(0, 2))


if __name__ == "__main__":
    unittest.main()
