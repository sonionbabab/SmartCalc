import unittest

from calculator import Calculator
from scientific import ScientificCalculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.sci = ScientificCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.calculate(5, "+", 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate(5, "-", 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate(5, "*", 3), 15)

    def test_division(self):
        self.assertEqual(self.calc.calculate(10, "/", 2), 5)

    def test_power(self):
        self.assertEqual(self.calc.calculate(2, "**", 3), 8)

    def test_square_root(self):
        self.assertEqual(self.sci.calculate("sqrt", 25), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(10, "/", 0)


if __name__ == "__main__":
    unittest.main()
