import unittest
from Calculador import Calculator


class TestCalculator(unittest.TestCase):

    def test_suma_2_mas_2_(self):
        cal = Calculator()
        self.assertEqual(4, cal.suma(2, 2))

    def test_suma_2_mas_4_(self):
        cal = Calculator()
        self.assertEqual(6, cal.suma(2, 4))

    def test_menos_2_2_(self):
        cal = Calculator()
        self.assertEqual(0, cal.resta(2, 2))

    def test_menos_3_2_(self):
        cal = Calculator()
        self.assertEqual(5, cal.resta(7, 2))

    def test_multiplica_2_2_(self):
        cal = Calculator()
        self.assertEqual(4, cal.multiplicacion(2, 2))

    def test_multiplica_2_9_(self):
        cal = Calculator()
        self.assertEqual(18, cal.multiplicacion(2, 9))

    def test_division_2_2_(self):
        cal = Calculator()
        self.assertEqual(1, cal.division(2, 2))

    def test_division_1_2_(self):
        cal = Calculator()
        self.assertEqual(3, cal.division(9, 3))

if __name__ == "__main__":
    unittest.main()
