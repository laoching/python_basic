from unittest import *
import calc2


class SeparateFormulaTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc2.separate_formula('3+1'), [3, '+', 1])

    def test_minus_oper(self):
        self.assertEqual(calc2.separate_formula('3-1'), [3, '-', 1])

    def test_multiple_oper(self):
        self.assertEqual(calc2.separate_formula('3*1'), [3, '*', 1])

    def test_division_oper(self):
        self.assertEqual(calc2.separate_formula('2/2'), [2, '/', 2])

    def test_complex_oper(self):
        self.assertEqual(calc2.separate_formula('2/2*2+1'), [2, '/', 2, '*', 2, '+', 1])
        self.assertEqual(calc2.separate_formula('12*2+1'), [12, '*', 2, '+', 1])


class CalcTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc2.calc([3, '+', 1]), 4)

    def test_minus(self):
        self.assertEqual(calc2.calc([3, '-', 1]), 2)

    def test_multiple(self):
        self.assertEqual(calc2.calc([3, '*', 1]), 3)

    def test_division(self):
        self.assertEqual(calc2.calc([2, '/', 2]), 1)

    def test_complex_calc(self):
        self.assertEqual(calc2.calc([2, '/', 2, '*', 2, '+', 1]), 3)
        self.assertEqual(calc2.calc([12, '*', 2, '+', 1]), 25)
