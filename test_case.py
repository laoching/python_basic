# 계산기
# 3+3, 3-3과 같이 입력하세요.
# +, -, /, *, 총 4가지 연산을 지원합니다.
from unittest import *
import calc2

class CustomTests(TestCase):
    def test_plus(self):
        self.assertEqual(calc2.separate_formula('3+1'),[3, '+', 1])
        self.assertEqual(calc2.calc([3, '+', 1]), 4)
    def test_minus(self):
        self.assertEqual(calc2.separate_formula('3-1'), [3, '-', 1])
        self.assertEqual(calc2.calc([3, '-', 1]), 2)
    def test_multiple(self):
        self.assertEqual(calc2.separate_formula('3*1'), [3, '*', 1])
        self.assertEqual(calc2.calc([3, '*', 1]), 3)
    def test_division(self):
        self.assertEqual(calc2.separate_formula('2/2'), [2, '/', 2])
        self.assertEqual(calc2.calc([2, '/', 2]), 1)
    def test_complex_calc(self):
        self.assertEqual(calc2.separate_formula('2/2*2+1'), [2, '/', 2, '*', 2, '+', 1])
        self.assertEqual(calc2.calc([2, '/', 2, '*', 2, '+', 1]), 3)
        self.assertEqual(calc2.separate_formula('12*2+1'), [12, '*', 2, '+', 1])
        self.assertEqual(calc2.calc([12, '*', 2, '+', 1]), 25)

if __name__ == '__main__':
    main()